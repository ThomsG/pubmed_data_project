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
print("Loading data...")

extract = Extraction("data/input")



# Appliquer la fonction à la colonne 'date'
extract.clinical_trials['date'] = extract.clinical_trials['date'].apply(lambda x: Transformation.harmonize_date(str(x)) if x else None)

print(extract.clinical_trials)


print(extract.drugs)
print(extract.pubmed_csv)
print(extract.pubmed_json)



