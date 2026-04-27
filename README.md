# Patent Big Data Processing Project

##Project Overview

This project focuses on processing and analyzing large-scale patent datasets using Python. The goal is to efficiently load, clean, and analyze big data while handling performance challenges such as memory limitations.

---

##Project Structure

```
Patent_BigData/
│── pipeline.ipynb        # Main data processing notebook
│── outputs/              # Generated results and analysis outputs
│── scripts/              # Supporting scripts (if any)
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* Jupyter Notebook
* SQL (for schema design)

---

##Key Features

### 1. Large File Handling

* Implemented **chunking** using Pandas (`chunksize`) to process very large `.tsv` files without running out of memory.

### 2. Data Cleaning

* Selected relevant columns from large datasets
* Handled missing values
* Structured data for analysis

### 3. Data Processing Pipeline

* End-to-end workflow implemented in `pipeline.ipynb`
* Includes:

  * Data loading
  * Transformation
  * Aggregation

### 4. Output Generation

* Processed results are saved in the `outputs/` folder

---

##How Chunking Works

Instead of loading entire datasets into memory, the system:

1. Reads data in small chunks
2. Processes each chunk independently
3. Combines results

This improves:

* Performance
* Memory efficiency
* Scalability

---

##How to Run the Project

1. Open the notebook:

   ```
   pipeline.ipynb
   ```
2. Run all cells step by step

---

## Notes

* Large raw datasets are **not included** due to size limitations
* Ensure dataset paths are correctly configured before running

---

## Results

* Cleaned and processed patent datasets
* Outputs stored in the `outputs/` directory

---

## Conclusion

This project demonstrates how to handle big data efficiently using Python by applying chunking and structured data processing techniques.

---
