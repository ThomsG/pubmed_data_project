import pandas as pd
import os
import json

class Extraction:
    def __init__(self, data_folder: str):
        self.data_folder = data_folder
        self.clinical_trials = None
        self.drugs = None
        self.pubmed_csv = None
        self.pubmed_json = None

        self._load_data()

    def _load_data(self):
        # Charger clinical_trials.csv
        clinical_trials_path = os.path.join(self.data_folder, "clinical_trials.csv")
        self.clinical_trials = pd.read_csv(clinical_trials_path)

        # Charger drugs.csv
        drugs_path = os.path.join(self.data_folder, "drugs.csv")
        self.drugs = pd.read_csv(drugs_path)

        # Charger pubmed.csv
        pubmed_csv_path = os.path.join(self.data_folder, "pubmed.csv")
        self.pubmed_csv = pd.read_csv(pubmed_csv_path)

        # Charger pubmed.json
        pubmed_json_path = os.path.join(self.data_folder, "pubmed.json")
        with open(pubmed_json_path, encoding="utf-8") as f:
            self.pubmed_json = pd.DataFrame(json.load(f))