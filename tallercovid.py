import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url) 

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)

aux = data['Ubicación del caso'].value_counts()

data.loc[data['Estado'] == 'leve','Estado'] = 'Leve'
data.loc[data['Estado'] == 'LEVE','Estado'] = 'Leve'

data.loc[data['Ubicación del caso'] == 'casa','Ubicación del caso'] = 'Casa'
data.loc[data['Ubicación del caso'] == 'CASA','Ubicación del caso'] = 'Casa'

data.loc[data['Sexo'] == 'm','Sexo'] = 'M'
data.loc[data['Sexo'] == 'f','Sexo'] = 'F'

data.loc[data['Edad'] == 'Casa','Edad'] = 36
data.loc[data['Edad'] == 'Leve','Edad'] = 36
data.loc[data['Edad'] == 'M','Edad'] = 36
data.loc[data['Edad'] == 'F','Edad'] = 36
