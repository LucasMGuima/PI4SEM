#    Gera o arquivo txt com o link para o exercicio
#    e o nome dos intgrantes do grupo
import os

def gerarTexto(link):
    text = """Link: {0}
Integrantes:
    Lucas da Mata,
    Raphael Shodi
            """.format(link)
    return text

def gerarEntrega(link, nome):
    # Abre o arquivo
    path = "{1}\Entrega\{0}.txt".format(nome, os.curdir)
    file = open(path, "w")

    #prepara o string
    file.write(gerarTexto(link))
    file.close()

print("====CRIADOS DE ENTREGA 3000====")
nome = input("Nome do arquivo: ")
link = input("Link do repositorio: ")
gerarEntrega(link, nome)