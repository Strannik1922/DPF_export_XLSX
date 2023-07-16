import pandas as pd


df_json = pd.read_json('C:/Dev/DPF_export_XLSX/well_2253.json')
df_json.to_excel('C:/Dev/DPF_export_XLSX/well_2253.xlsx')
