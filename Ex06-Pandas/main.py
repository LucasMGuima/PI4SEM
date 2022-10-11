import pandas as pd
import math

#Importa os dados, sem cabecalho
df_seeds = pd.read_csv("https://raw.githubusercontent.com/celsocrivelaro/simple-datasets/main/seeds.csv", header=None)

#Seta um cabecalho
cabecalho = ['Área A',
             'Perímetro P',
             'Extensão do núcleo',
             'Largura',
             'Coeficiente de Assimetria',
             'Extensão do sulgo do núcleo','1','2','3']
df_seeds.columns = cabecalho

#Remove as colunas extras no final
df_seeds = df_seeds.drop('1',axis=1)
df_seeds = df_seeds.drop('2',axis=1)
df_seeds = df_seeds.drop('3',axis=1)

#Remove elementos com campos Na
df_seeds.dropna(inplace=True)

#Adicionar um novo campo
def calc_compactacao(A, P):
    #C = 4*pi*A/P^2
    c = (4*math.pi*A)/P**2
    return c

df_seeds['Compactação'] = calc_compactacao(df_seeds['Área A'], df_seeds['Perímetro P'])

#Exporta para um CSV
df_seeds.to_csv('output/out.csv',index=False,encoding = 'utf-8')