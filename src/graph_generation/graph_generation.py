import json
import os
import pandas as pd

class GraphGeneration:
    def __init__(self, clinical_trials_df, drugs_df, pubmed_df_csv, pubmed_df_json):
        self.clinical_trials_df = clinical_trials_df
        self.drugs_df = drugs_df
        self.pubmed_df = pd.concat([pubmed_df_csv, pubmed_df_json], ignore_index=True)
        self.graph = None

        self._build_graph()

    def _build_graph(self):
        # Builds a graph linking drugs, journals, pubmed, and clinical trials
        
        graph = {"drugs": []}

        for _, drug_row in self.drugs_df.iterrows():
            drug_name = str(drug_row['drug']).lower()
            drug_node = {
                "drug": drug_row['drug'],
                "references": {},  # {"pubmed": [dates], "clinical_trials": [dates]}
                "journals": {}     # {"journal_name": [dates]}
            }

            # PubMed
            for _, pub_row in self.pubmed_df.iterrows():
                if drug_name in str(pub_row['title']).lower():
                    drug_node["references"].setdefault("pubmed", []).append(pub_row['date'])
                    journal = pub_row['journal']
                    drug_node["journals"].setdefault(journal, []).append(pub_row['date'])

            # Clinical trials
            for _, ct_row in self.clinical_trials_df.iterrows():
                if drug_name in str(ct_row['scientific_title']).lower():
                    drug_node["references"].setdefault("clinical_trials", []).append(ct_row['date'])
                    journal = ct_row['journal']
                    drug_node["journals"].setdefault(journal, []).append(ct_row['date'])

            # Remove duplicates in references and journals
            for ref in drug_node["references"]:
                drug_node["references"][ref] = list(dict.fromkeys(drug_node["references"][ref]))
            for journal in drug_node["journals"]:
                drug_node["journals"][journal] = list(dict.fromkeys(drug_node["journals"][journal]))

            graph["drugs"].append(drug_node)
        
        self.graph = graph

    def export_graph_to_json(graph):
        with open('data/output/final_graph.json', "w", encoding="utf-8") as f:
            json.dump(graph, f, ensure_ascii=False, indent=2)