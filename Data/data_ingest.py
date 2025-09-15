# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Dataset handle
handle = "nishanthsalian/socioeconomic-country-profiles"

# Optionally set a specific path inside the dataset (e.g., "data.csv").
# Leave empty to auto-discover a suitable file.
file_path = ""

def _find_supported_file(root_dir: str) -> str:
  supported = {
    ".csv", ".tsv", ".json", ".jsonl", ".xml", ".parquet", ".feather",
    ".xls", ".xlsx", ".xlsm", ".xlsb", ".odf", ".ods", ".odt",
  }
  # Prefer lighter, common tabular formats first
  preferred_order = [
    ".csv", ".tsv", ".parquet", ".feather", ".xlsx", ".xls", ".jsonl", ".json",
    ".xml", ".xlsm", ".xlsb", ".odf", ".ods", ".odt",
  ]
  candidates_by_ext = {ext: [] for ext in preferred_order}
  for dirpath, _, filenames in os.walk(root_dir):
    for name in filenames:
      ext = os.path.splitext(name)[1].lower()
      if ext in supported:
        candidates_by_ext.setdefault(ext, []).append(os.path.join(dirpath, name))
  for ext in preferred_order:
    if candidates_by_ext.get(ext):
      return candidates_by_ext[ext][0]
  raise FileNotFoundError("No supported data files found in downloaded dataset.")

if not file_path:
  dataset_root = kagglehub.dataset_download(handle)
  picked_file_abs = _find_supported_file(dataset_root)
  file_path = os.path.relpath(picked_file_abs, dataset_root)
  print(f"Auto-selected dataset file: {file_path}")

# Load using the non-deprecated API
df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  handle,
  file_path,
)

print("First 5 records:", df.head())