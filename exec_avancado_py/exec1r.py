arquivo = "tarefas.txt"

while True:
    print("\n1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")

    op = input("Escolha: ")

    if op == "1":
        tarefa = input("Digite a tarefa: ")
        with open(arquivo, "a") as f:
            f.write(tarefa + "\n")

    elif op == "2":
        try:
            with open(arquivo, "r") as f:
                tarefas = f.readlines()

                if len(tarefas) == 0:
                    print("Nenhuma tarefa.")
                else:
                    for i, t in enumerate(tarefas, start=1):
                        print(f"{i} - {t.strip()}")
        except:
            print("Arquivo ainda não existe.")

    elif op == "3":
        break

    else:
        print("Opção inválida")