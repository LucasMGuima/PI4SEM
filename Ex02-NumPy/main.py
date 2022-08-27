import numpy as np

alturas = np.loadtxt(".\\Arquivos\\altura.txt")
anos = np.loadtxt(".\\Arquivos\\anos.txt")

cont = 0
qtd_alturas = 0
soma_altura = 0
for ano in anos:
    if(int(ano) > 1998 and int(ano) < 2005):
        soma_altura += float(alturas[cont])
        qtd_alturas += 1
    cont += 1

media = soma_altura/qtd_alturas