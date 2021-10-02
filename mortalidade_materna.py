import pandas as pd
from datetime import date
import numpy as np

df = pd.read_csv("DOMAT20.csv", dtype=str, usecols=["DTOBITO", "IDADE", "RACACOR", "LOCOCOR", "CODESTAB", "CODMUNOCOR", "TPMORTEOCO", "OBITOGRAV", "CAUSABAS"])

df["DTOBITO"] = df["DTOBITO"].apply(pd.to_datetime, errors='coerce', format='%d%m%Y')

df['IDADE'] = df['IDADE'].replace('4', '', regex=True)

df['RACACOR'] = df['RACACOR'].replace({'1':'Branca', '2':'Preta', '3':'Amarelo', '4':'Parda', '5':'Indígina'})

df['LOCOCOR'] = df['LOCOCOR'].replace({'9':'Ignorado', '1':'Hospital', '2':'Outro Estab Saúde', '3':'Domicílio', '4':'Via Pública', '5': 'Outros'})

df['TPMORTEOCO'] = df['TPMORTEOCO'].replace({'1':'Na gravidez', '2':'No parto', '3':'No aborto', '4':'Até 42 dias após o parto', '5':'De 43 dias a 1 ano após o parto', '8':'Não ocorreu nestes períodos', '9':'Ignorado'})

df['OBITOGRAV'] = df['OBITOGRAV'].replace({'9':'Ignorado', '1':'Sim', '2':'Não'})

df.head()
