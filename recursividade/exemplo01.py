def funcaoA(valor):
    if valor != 5:
        print("A")
        print(valor)
        funcaoA(valor+1)
        print(f"final A {valor}")
    else:
        print("caso base")

def funcaoB(valor):
    print("B")
    print(valor)

if __name__ == "__main__":
    funcaoA(1)
    print("acabou")