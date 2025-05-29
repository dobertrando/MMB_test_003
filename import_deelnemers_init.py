import pandas as pd
import django
import os
import openpyxl

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmb.settings')
django.setup()

from deelnemers.models import Deelnemer

bestand = os.path.join('deelnemers', 'data', 'project_mmb_data.xlsx')

df = pd.read_excel(bestand, sheet_name='deelnemers')

for idx, row in df.iterrows():
    deelnemer = Deelnemer(
        voornaam=row['Voornaam'],
        achternaam=row['Achternaam'],
        naamvoornaam=f"{row['Voornaam']} {row['Achternaam']}",
        status=row.get('Status', 'Actief'),
        ploegnaam=row.get('PloegNaam', 'Geen ploegnaam'),
        clan=row.get('Clan', 'Geen clan'),

    )
    
    deelnemer.save()
    print(f"Toegevoegd: {deelnemer.naamvoornaam}")

