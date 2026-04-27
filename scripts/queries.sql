-- Q1: Top Inventors
SELECT inventor_id, COUNT(*) AS total_patents
FROM inventors
GROUP BY inventor_id
ORDER BY total_patents DESC
LIMIT 10;

-- Q2: Top Companies
SELECT disambig_assignee_organization, COUNT(*) AS total
FROM assignees
GROUP BY disambig_assignee_organization
ORDER BY total DESC
LIMIT 10;

-- Q3: Top Countries
SELECT country, COUNT(*) AS total
FROM inventors
WHERE country IS NOT NULL AND country != ''
GROUP BY country
ORDER BY total DESC
LIMIT 10;

-- Q4: Trends Over Time
SELECT year, COUNT(*) AS total
FROM patents
GROUP BY year
ORDER BY year;

-- Q5: JOIN Query
SELECT p.patent_id, i.inventor_id, a.disambig_assignee_organization
FROM patents p
JOIN inventors i ON p.patent_id = i.patent_id
JOIN assignees a ON p.patent_id = a.patent_id
LIMIT 10;

-- Q6: CTE Query
WITH inventor_counts AS (
SELECT inventor_id, COUNT(*) AS total
FROM inventors
GROUP BY inventor_id
)
SELECT *
FROM inventor_counts
ORDER BY total DESC
LIMIT 10;

-- Q7: Ranking Query
SELECT inventor_id, total,
RANK() OVER (ORDER BY total DESC) as rank
FROM (
SELECT inventor_id, COUNT(*) as total
FROM inventors
GROUP BY inventor_id
);
