import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

path_csv = './csv/FAO.csv'
output_csv_path = './csv/FAO_cleaned.csv'

# Création du dataframe via le csv
dataframe = pd.read_csv(path_csv, encoding='ISO-8859-1')

# Check des doublons
duplicated_lines = dataframe[dataframe.duplicated()]

if not duplicated_lines.empty:
    dataframe.drop_duplicates(inplace=True) #Supprime les doublons
else:
    print("Aucune ligne identique dans le dataframe.")


# Check des valeurs = 0
get_null = dataframe.isnull().sum()
for col, count in get_null.items():
    print(f"Le nombre de valeurs manquantes de {col} est {count}")
    if count > 0:
        print(f"Colonnes: {col}")


# Check des valeurs manquantes
empty_cells = dataframe.isna()
if empty_cells.any().any():
    dataframe.replace('', np.nan, inplace=True)
else:
    print("Il n'y a aucune valeur manquante")

dataframe.reset_index(drop=True, inplace=True)
# dataframe.to_csv(output_csv_path, index=False)


# Check des données aberrantes avec Boite a Moustache
columns_to_convert = dataframe.columns[10:64]
dataframe[columns_to_convert] = dataframe[columns_to_convert].apply(pd.to_numeric, errors='coerce')
columns_to_plot = dataframe.columns[10:64] 

plt.figure(figsize=(16, 8))

for col in columns_to_plot:
    plt.boxplot(dataframe[col].dropna(), vert=False, positions=[columns_to_plot.get_loc(col)])
    
plt.yticks(range(1, len(columns_to_plot) + 1), columns_to_plot)
plt.title("Boxplots pour chaque colonne des colonnes 11 à 63")
plt.show()







