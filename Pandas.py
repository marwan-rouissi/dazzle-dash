import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cProfile as cp
import dash_bootstrap_components as dbc

# Read the CSV file into a DataFrame: df
CSV_PATH = 'CSV/FAO.csv'
df = pd.read_csv(CSV_PATH, encoding='ISO-8859-1')
# print(df.head(10))

# Check out info of df
# print(df.info())
isNull = df.isnull().sum()
# for i in range(len(isNull)):
#     if isNull[i] > 0:
#         print(df.columns[i], isNull[i])
# totalNotNull = df.notnull().sum().sum()
# totalNull = df.isnull().sum().sum()
# totalValue = totalNotNull + totalNull
# print("Total value: ", totalValue)
# print("Total not null value: ", totalNotNull)
# print("Total null value: ", totalNull)
# count the number of total observation in Area column
# print("\n",df['Area'].count())

#type of data in each column
Qualitative = []
Discrete = []
Continue = []
Qualitative_Obs = "Chaque donnée qualitative est de nature Nominal, car elle ne permettent pas de ranger les données dans un ordre autre qu'alphabétiquement. \n"
Discrete_Obs = "Les données discrètes sont des valeurs fixes définient, elle n'appartiennent pas à un intervalle de valeurs.\n"
Continue_Obs = "Les données continues sont des valeurs qui peuvent prendre n'importe quelle valeur dans un intervalle donné, elles servent de mesure d'unités de nourriture produite ou consommé dans notre cas.\n"
print(df.dtypes)
# Transform the types of data in the 2 last columns
df['Y2012'] = df['Y2012'].astype('float64')
df['Y2013'] = df['Y2013'].astype('float64')
for i in range(len(df.dtypes)):
    if df.dtypes[i] == 'object':
        Qualitative.append(df.columns[i])
    if df.dtypes[i] == 'int64':
        Discrete.append(df.columns[i])
    if df.dtypes[i] == 'float64':
        Continue.append(df.columns[i])

print("Qualitative: ", Qualitative)
print(Qualitative_Obs)
print("Discrete: ", Discrete)
print(Discrete_Obs)
print("Continue: ", Continue)
print(Continue_Obs)
