import os
import pandas as pd
import json
import shutil

class Verification:
    def __init__(self, data_folder):
        self.data_folder = data_folder
        self.invalid_files = self.file_verification_and_move()
        
    # Check files validity, print invalid ones and move them in another folder named "bad_input"
    def file_verification_and_move(self):
        invalid_files = []
        invalid_file_folder = os.path.join(self.data_folder, "../bad_input")
        os.makedirs(invalid_file_folder, exist_ok=True)

        for filename in os.listdir(self.data_folder):
            path = os.path.join(self.data_folder, filename)
            
            is_invalid = False
            if filename.endswith('.csv'):
                try:
                    pd.read_csv(path)
                except Exception:
                    is_invalid = True
            elif filename.endswith('.json'):
                try:
                    with open(path, encoding="utf-8") as f:
                        json.load(f)
                except Exception:
                    is_invalid = True
                    
            if is_invalid:
                invalid_files.append(filename)
                shutil.move(path, os.path.join(invalid_file_folder, filename))
        return invalid_files