import numpy as np

#Cria arrays com as informações no txt
alturas = np.loadtxt(".\\Arquivos\\altura.txt")
anos = np.loadtxt(".\\Arquivos\\anos.txt")

#Variaveis usadas para coletar as alturas
cont = 0
list_altura = list()

#Pega as alturas com base nos anos
for ano in anos:
    if(int(ano) > 1998 and int(ano) < 2005):
        list_altura.append(alturas[cont])
    cont += 1

#Transforma a lista em NumPy.Array
amostra_alturas = np.array(list_altura)

#Calcula a media
media = np.mean(amostra_alturas)

print("Media:", round(media, 3),"cm")