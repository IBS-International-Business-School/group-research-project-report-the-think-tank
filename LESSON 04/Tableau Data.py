import pandas as pd
import numpy as np
from datetime import datetime

# Load all CSV files
villagers = pd.read_csv('villagers.csv', encoding='utf-8-sig')
fish = pd.read_csv('fish.csv', encoding='utf-8-sig')
insects = pd.read_csv('insects.csv', encoding='utf-8-sig')
fossils = pd.read_csv('fossils.csv', encoding='utf-8-sig')
art = pd.read_csv('art.csv', encoding='utf-8-sig')
achievements = pd.read_csv('achievements.csv', encoding='utf-8-sig')
reactions = pd.read_csv('reactions.csv', encoding='utf-8-sig')

# Create a master Excel file for Tableau
with pd.ExcelWriter('Animal_Crossing_Data.xlsx', engine='openpyxl') as writer:
    villagers.to_excel(writer, sheet_name='Villagers', index=False)
    fish.to_excel(writer, sheet_name='Fish', index=False)
    insects.to_excel(writer, sheet_name='Insects', index=False)
    fossils.to_excel(writer, sheet_name='Fossils', index=False)
    art.to_excel(writer, sheet_name='Art', index=False)
    achievements.to_excel(writer, sheet_name='Achievements', index=False)
    reactions.to_excel(writer, sheet_name='Reactions', index=False)

print("Master Excel file created for Tableau!")