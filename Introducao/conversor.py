def metros_pes():
    metros = int(input("Entre com os metros: "))
    pes = metros * 3.281
    print(str(metros) + "m -> " + str(pes) + "pés")

def pes_metros():
    pes = int(input("Entre com os pes: "))
    metros = pes * 0.3048
    print(str(pes) + "pés -> " + str(metros) + "m")

def conversor_medidas():
    opcoes = {1: metros_pes, 2: pes_metros}
    while True:
        print("\nEscolha o tipo de conversão")
        print("1 - Metros -> Pés")
        print("2 - Pés -> Metros")
        print("0 - Sair")
        entrada = int(input("Opição: "))

        if(entrada == 0):
            print("Bye!!")
            return

        if entrada < 3 : opcoes[entrada]()
    
