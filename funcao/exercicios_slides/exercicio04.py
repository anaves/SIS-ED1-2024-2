numeros = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "tres": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "quatorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20,
    "trinta": 30,
    "quarenta": 40,
    "cinquenta": 50,
    "sessenta": 60,
    "setenta": 70,
    "oitenta": 80,
    "noventa": 90
}

extenso = input("digite um numero por extenso: ")
extenso = extenso.replace(" e ", " ")
print(extenso)
partes = extenso.split(" ")
print(partes)

numero = 0
print("------parcial------")
for parte in partes:
    valor = numeros[parte]
    numero += valor
    print(numero)

print('-----final-----')
print(numero)