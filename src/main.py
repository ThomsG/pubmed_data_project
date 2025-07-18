from extraction.extraction import Extraction
from verification.verification import Verification

# Checking file validity
print("Checking file validity...")

invalid_files = Verification("data/input")
if invalid_files:
    print("Invalid files:", invalid_files)
else:
    print("All files are valid.")

# Extracting data from input files
print("Loading data...")

extract = Extraction("data\input")

print(extract.clinical_trials.head())
print(extract.drugs.head())
print(extract.pubmed_csv.head())
print(extract.pubmed_json.head())

