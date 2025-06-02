import os
import pandas as pd
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmb.settings')
django.setup()

from koersen.models import KoersEditie, Koers
from deelnemers.models import Deelnemer

bestand = os.path.join('deelnemers', 'data', 'project_mmb_data.xlsx')

df = pd.read_excel(bestand, sheet_name='uitslagen')

for idx, row in df.iterrows():
    eerste_plaats_str = row['eerste_plaats']
    if pd.notna(row['eerste_plaats']):
        namen_eerste_plaats = [naam.strip() for naam in row['eerste_plaats'].split(';')]
        eerste_plaats=Deelnemer.objects.filter(naamvoornaam__in=namen_eerste_plaats)
    else:
        eerste_plaats=None,
    tweede_plaats_str = row['tweede_plaats']
    if pd.notna(row['tweede_plaats']):
        namen_tweede_plaats = [naam.strip() for naam in row['tweede_plaats'].split(';')]
        tweede_plaats=Deelnemer.objects.filter(naamvoornaam__in=namen_tweede_plaats)
    else:
        tweede_plaats=None,
    derde_plaats_str = row['derde_plaats']
    if pd.notna(row['derde_plaats']):
        namen_derde_plaats = [naam.strip() for naam in row['derde_plaats'].split(';')]
        derde_plaats=Deelnemer.objects.filter(naamvoornaam__in=namen_derde_plaats)
    else:
        derde_plaats=None,


    koers_editie = KoersEditie(
        jaar=row['Jaar'],
        koers=Koers.objects.get(naam=row['KoersNaam']),
        editie=row['Editie'],
        koersstatus=row['KoersStatus'],
        uitslagstatus=row['UitslagStatus']
    )

    koers_editie.save()
    koers_editie.eerste_plaats.set(eerste_plaats)
    koers_editie.tweede_plaats.set(tweede_plaats)
    koers_editie.derde_plaats.set(derde_plaats)
    print(f"Toegevoegd: {koers_editie.koers.naam} {koers_editie.editie} ({koers_editie.jaar})")
    
