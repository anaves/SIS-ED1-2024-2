def funcaoA(valor):
    if valor != 30:
        print("A")
        print(valor)
        funcaoA(valor+1)
        print("final A")
    else:
        print("caso base")

def funcaoB(valor):
    print("B")
    print(valor)

if __name__ == "__main__":
    funcaoA(10)