from numerizer import numerize
from deep_translator import GoogleTranslator

tradutor =  GoogleTranslator(source="pt", target="en")
texto = input("digite o texto: ")
traduzido = tradutor.translate(texto)
print(traduzido)
numero = numerize(traduzido)
print(numero)