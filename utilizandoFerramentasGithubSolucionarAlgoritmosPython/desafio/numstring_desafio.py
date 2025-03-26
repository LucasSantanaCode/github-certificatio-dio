# Solicitar uma string e um numero inteiro como entrada. retornar a string repetida o numero de vezes informado
string = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))
strnum = string * numero
print(f"A string repetida {numero} vezes é: {(string + " ") * numero } ")