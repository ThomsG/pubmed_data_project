from extraction.extraction import Extraction
from verification.verification import Verification
from transformation.transformation import Transformation

# Checking file validity
print("Checking file validity...")

invalid_files = Verification("data/input")
if invalid_files:
    print("Invalid files:", invalid_files)
else:
    print("All files are valid.")

# Extracting data from input files
print("Extracting data...")

extract = Extraction("data/input")

# Transforming data by cleaning them
print("Transforming data...")

extract.clinical_trials = Transformation.harmonize_date(extract.clinical_trials, 'date')
extract.clinical_trials = Transformation.clean_text_encoding_issues(extract.clinical_trials, 'journal')
extract.clinical_trials = Transformation.clean_text_encoding_issues(extract.clinical_trials, 'scientific_title')
extract.clinical_trials = Transformation.merge_rows(extract.clinical_trials, 'scientific_title')

extract.pubmed_csv = Transformation.harmonize_date(extract.pubmed_csv, 'date')
extract.pubmed_json = Transformation.harmonize_date(extract.pubmed_json, 'date')
extract.pubmed_json = Transformation.fill_missing_ids(extract.pubmed_json, 'id')

print(extract.clinical_trials)
print(extract.drugs)
print(extract.pubmed_csv)
print(extract.pubmed_json)
