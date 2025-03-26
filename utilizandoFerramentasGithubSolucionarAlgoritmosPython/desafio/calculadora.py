# Solicitar 2 numeros, solicitar que operação o usuario deseja realizar, retornar o resultado da operação escolhida

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    print(f"O resultado da soma é: {num1 + num2}")
elif operacao == "-":
    print(f"O resultado da subtração é: {num1 - num2}")
elif operacao == "*":
    print(f"O resultado da multiplicação é: {num1 * num2}")
elif operacao == "/":
    print(f"O resultado da divisão é: {num1 / num2}")
else:
    print("Operação inválida")
