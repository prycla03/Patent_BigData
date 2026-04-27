import pandas as pd
import sqlite3
import os

DATA_DIR = "../data"
DB_PATH = "../database/patents.db"

PATENT_FILE = os.path.join(DATA_DIR, "g_patent.tsv")
INVENTOR_FILE = os.path.join(DATA_DIR, "g_inventor_disambiguated.tsv")
ASSIGNEE_FILE = os.path.join(DATA_DIR, "g_assignee_disambiguated.tsv")
USPC_FILE = os.path.join(DATA_DIR, "g_uspc_at_issue.tsv")

CHUNK_SIZE = 100_000
START_YEAR = 2000
END_YEAR = 2020


def load_patents():
    results = []

    for chunk in pd.read_csv(
        PATENT_FILE,
        sep='\t',
        usecols=['patent_id', 'patent_date'],
        chunksize=CHUNK_SIZE,
        low_memory=False
    ):
        chunk['patent_date'] = pd.to_datetime(chunk['patent_date'], errors='coerce')
        chunk['year'] = chunk['patent_date'].dt.year

        filtered = chunk[
            (chunk['year'] >= START_YEAR) &
            (chunk['year'] <= END_YEAR)
        ]

        results.append(filtered)

    patents = pd.concat(results, ignore_index=True)
    print(f"Patents loaded: {patents.shape}")

    return patents


def filter_by_patent_ids(file_path, usecols, valid_ids):
    results = []

    for chunk in pd.read_csv(
        file_path,
        sep='\t',
        usecols=usecols,
        chunksize=CHUNK_SIZE,
        low_memory=False
    ):
        filtered = chunk[chunk['patent_id'].isin(valid_ids)]
        results.append(filtered)

    return pd.concat(results, ignore_index=True)


def main():
    print("Starting data pipeline...")

    # Connect to database
    conn = sqlite3.connect(DB_PATH)

    # Step 1: Load patents
    patents = load_patents()
    valid_ids = set(patents['patent_id'])

    # Step 2: Load related tables
    inventors = filter_by_patent_ids(
        INVENTOR_FILE,
        ['patent_id', 'inventor_id'],
        valid_ids
    )

    assignees = filter_by_patent_ids(
        ASSIGNEE_FILE,
        ['patent_id', 'disambig_assignee_organization'],
        valid_ids
    )

    uspc = filter_by_patent_ids(
        USPC_FILE,
        ['patent_id', 'uspc_mainclass_id'],
        valid_ids
    )

    print("Inventors:", inventors.shape)
    print("Assignees:", assignees.shape)
    print("USPC:", uspc.shape)

    # Step 3: Save to SQL
    patents.to_sql("patents", conn, if_exists="replace", index=False)
    inventors.to_sql("inventors", conn, if_exists="replace", index=False)
    assignees.to_sql("assignees", conn, if_exists="replace", index=False)
    uspc.to_sql("uspc", conn, if_exists="replace", index=False)

    # Step 4: Build relationships table
    relationships = pd.merge(inventors, assignees, on="patent_id", how="inner")
    relationships.to_sql("relationships", conn, if_exists="replace", index=False)

    print("Relationships:", relationships.shape)

    conn.close()
    print("✅ Data pipeline completed successfully!")


if __name__ == "__main__":
    main()