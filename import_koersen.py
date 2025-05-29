import pandas as pd
import django
import os
import openpyxl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmb.settings')
django.setup()

from koersen.models import Koers

bestand = os.path.join('deelnemers', 'data', 'project_mmb_data.xlsx')

df = pd.read_excel(bestand, sheet_name='koers')

for idx, row in df.iterrows():
    koers = Koers(
        naam=row['Naam'],
        niveau=row['Niveau'],
        afkorting=row['Afkorting'],
        land=row['Land'],
        koersvolgnummer=row['Koersvolgnummer']
    )
    
    koers.save()
    print(f"Toegevoegd: {koers.naam} ({koers.afkorting})")


