n = int(input("Quantos números? "))

if n > 0:
    lista = []

    for i in range(n):
        num = float(input("Digite um número: "))
        lista.append(num)

    print("Maior:", max(lista))
    print("Menor:", min(lista))
    print("Média:", sum(lista)/len(lista))
else:
    print("Valor inválido")