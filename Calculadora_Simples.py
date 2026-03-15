print("Calculadora Simples v1")

valor1 = float(input("Informe o valor 1: "))
valor2 = float(input("Informe o valor 2: "))
op = str(input("Informe a operação (+, -, /, *, ^):  "))

if op == "+" or op == "-" or op == "*" or op == "/" or op == "^":
    if op == "/":
        if valor2 == 0:
            print("Não é possível dividir por 0")
        else:
            resultado = valor1 / valor2
            print("Resultado: ", resultado)
    if op == "+":
        resultado = valor1 + valor2
        print("Resultado: ", resultado)
    if op == "-":
        resultado = valor1 - valor2
        print("Resultado: ", resultado)
    if op == "*":
        resultado = valor1 * valor2
        print("Resultado: ", resultado)
    if op == "^":
        resultado = valor1 ** valor2
        print("Resultado: ", resultado)
else:
    print("Operador Inválido, tente novamente")
