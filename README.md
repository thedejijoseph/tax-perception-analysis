# Tax Morale Analysis - NESG Dataset

## Project Overview
This project involves analyzing the NESG Nigeria Tax Perception Dataset (Household and Firm) to predict Tax Morale and identify key socio-economic drivers. 
It uses a Machine Learning approach for the analysis and potentially includes an interactive dashboard.

## Setup Instructions

This project uses `uv` for dependency management.

1. Ensure `uv` is installed on your system.
2. Clone this repository and navigate to the project root.
3. Run the following command to synchronize the environment:

```bash
uv sync
```

4. To run the main analysis script:

```bash
uv run python main.py
```

## Directory Structure
- `data/raw/`: Original Codebooks and Datasets (not tracked by Git)
- `data/processed/`: Processed datasets and codebook mappings
- `notebooks/`: Jupyter Notebooks for Exploratory Data Analysis
- `src/`: Python scripts for data processing and modeling
- `reports/`: Research topic PDFs and generated figures/reports
