from extraction.extraction import Extraction
from verification.verification import Verification
from transformation.transformation import Transformation
from graph_generation.graph_generation import GraphGeneration
import os

# Checking file validity
print("Checking file validity...")

invalid_files = Verification("data/raw_input")
if invalid_files:
    print("Invalid files:", invalid_files) 
else:
    print("All files are valid.")

# Extracting data from raw input files
print("Extracting data...")

extract = Extraction("data/raw_input")

# Transforming data by cleaning them 
# (we assume that the data is inconsistent only identified columns where we applied transformations)
print("Transforming data...")

extract.clinical_trials = Transformation.harmonize_date(extract.clinical_trials, 'date')
extract.clinical_trials = Transformation.clean_text_encoding_issues(extract.clinical_trials, 'journal')
extract.clinical_trials = Transformation.clean_text_encoding_issues(extract.clinical_trials, 'scientific_title')
extract.clinical_trials = Transformation.merge_rows(extract.clinical_trials, 'scientific_title')

extract.pubmed_csv = Transformation.harmonize_date(extract.pubmed_csv, 'date')
extract.pubmed_json = Transformation.harmonize_date(extract.pubmed_json, 'date')
extract.pubmed_json = Transformation.fill_missing_ids(extract.pubmed_json, 'id')


# Save clean df as files to data/ready
print("Output processed data as files...")

ready_dir = os.path.join('data', 'processed')
os.makedirs(ready_dir, exist_ok=True)

extract.clinical_trials.to_csv(os.path.join(ready_dir, 'clinical_trials.csv'), index=False)
extract.drugs.to_csv(os.path.join(ready_dir, 'drugs.csv'), index=False)
extract.pubmed_csv.to_csv(os.path.join(ready_dir, 'pubmed.csv'), index=False)
extract.pubmed_json.to_json(os.path.join(ready_dir, 'pubmed.json'), orient='records', force_ascii=False, indent=2)

print('DataFrames successfully saved to path: data/processed/')

# Extracting data from ready files
print("Extracting processed data...")

extract = Extraction("data/processed")

# Generating the graph
print("Generating the graph...")
graph_gen = GraphGeneration(extract.clinical_trials, extract.drugs, extract.pubmed_csv, extract.pubmed_json)

# Exporting the graph
print("Exporting the graph as a JSON file...")
GraphGeneration.export_graph_to_json(graph_gen.graph)

print('Graph successfully saved to path: data/output/')