def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

op = int(input("Escolha: "))

a = float(input("Número 1: "))
b = float(input("Número 2: "))

if op == 1:
    print(somar(a, b))
elif op == 2:
    print(subtrair(a, b))
elif op == 3:
    print(multiplicar(a, b))
elif op == 4:
    print(dividir(a, b))
else:
    print("Opção inválida")