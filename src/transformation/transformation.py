import pandas as pd
from datetime import datetime

class Transformation:

# Fonction pour harmoniser la date
    def harmonize_date(date):
        # Essayer de convertir la date avec différents formats
        for format in ['%d %B %Y', '%d/%m/%Y', '%Y-%m-%d']:
            try:
                return datetime.strptime(date, format).strftime('%Y-%m-%d')
            except ValueError:
                continue
        return None  # Si le format est impossible à reconnaître