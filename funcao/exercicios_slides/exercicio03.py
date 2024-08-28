import os

def menu(mem):
    # os.system("cls")
    os.system("clear")
    print(f"Estado da memória: {mem}")
    print("Opções:")
    print()
    print("1- Somar")
    print("2- Subtrair")
    print("5- Limpar Memoria")
    print()
    return input("Qual opção você deseja? ")

def somar(x, y):
    return x+y

def calculadora():
    memoria = 0
    op = ""
    while op!= "6":
        op = menu(memoria)
        if op in ["1","2","3","4"]:
            valor = float(input("digite valor: "))
            if op == "1":
                memoria = somar(memoria, valor)
        elif op == "5":
            memoria = 0

calculadora()