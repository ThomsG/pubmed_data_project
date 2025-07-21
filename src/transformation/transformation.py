import pandas as pd
import re
from datetime import datetime

class Transformation:
        
    # Apply same date format 
    def harmonize_date(df, date_column):

        # Try to parse the date in various formats
        def reformat_date(val):
            for format in ['%d %B %Y', '%d/%m/%Y', '%Y-%m-%d']:
                try:
                    return datetime.strptime(val, format).strftime('%Y-%m-%d')
                except ValueError:
                    continue
            return None  # If no format matches, return None
        
        df[date_column] = df[date_column].apply(reformat_date)
        return df

    # Merge row info if they have the same business key
    def merge_rows(df, business_key):
        
        grouped = df.groupby([business_key]) # Group by the business key

        def coalesce(group_values):
            # Return the first non-null and non-empty value in the group list
            for val in group_values:
                if pd.notnull(val) and val != "":
                    return val
            return None
        
        merged_df = grouped.agg(coalesce).reset_index() # Aggregate the data and convert grouped object to DataFrame
        merged_df = merged_df[df.columns.tolist()] # Keep the original columns order
        return merged_df

    # Clean encoding issues in a specific column of a DataFrame
    def clean_text_encoding_issues(df, column):

        encoding_pattern = re.compile(r'\\xc3\\x[0-9a-fA-F]{2}') # Matches common encoding issues like \xc3\xb1

        def clean_text(val):
            if isinstance(val, str):
                return encoding_pattern.sub('', val)
            return val
        
        df[column] = df[column].apply(clean_text)
        return df
    
    def fill_missing_ids(df, id_col):
        
        df = df.copy()

        missing_mask = df[id_col].isnull() | (df[id_col] == "") # Identify empty or null ids 
        
        # Logic to generate negative ids based on the number of missing ids
        n_missing = missing_mask.sum()
        new_ids = [-i for i in range(1, n_missing + 1)]
        df.loc[missing_mask, id_col] = new_ids

        return df
        