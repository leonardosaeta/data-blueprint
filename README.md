# data-blueprint

## Overview
This project demonstrates a minimal, reproducible data workflow: ingesting a public dataset, performing exploratory data analysis (EDA), and running clustering (DBSCAN) on socioeconomic country indicators. The work is organized into small, focused notebooks and a lightweight ingest script.

## Data
- Source: Kaggle dataset `nishanthsalian/socioeconomic-country-profiles` (downloaded via KaggleHub).
- Local files in `Data/`:
  - `soci_econ_country_profiles.csv`: base tabular data used for exploration.
  - `dbscan_labels.csv`: saved cluster labels produced by the clustering notebook.
  - `data_ingest.py`: helper script to fetch and load the dataset using KaggleHub.

Note: Public datasets generally work without credentials, but some Kaggle datasets may require being logged in with KaggleHub.

## Notebooks
- `exploration.ipynb`: EDA, feature inspection, distributions, relationships, and data quality checks.
- `clustering.ipynb`: Feature selection, preprocessing, and DBSCAN clustering of countries; exports `dbscan_labels.csv`.

## Setup
Requires Python 3.10+.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage
1) Download/prepare data (optional if `Data/soci_econ_country_profiles.csv` already exists):
```bash
python Data/data_ingest.py
```

2) Launch notebooks:
```bash
jupyter lab
# or: jupyter notebook
```
Open `exploration.ipynb` for EDA, then `clustering.ipynb` to run DBSCAN and write `Data/dbscan_labels.csv`.

## Project structure
```text
data-blueprint/
  Data/
    data_ingest.py
    soci_econ_country_profiles.csv
    dbscan_labels.csv
  exploration.ipynb
  clustering.ipynb
  requirements.txt
  README.md
```
