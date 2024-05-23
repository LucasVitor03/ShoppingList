lista_compra = []

while True:

    print('-' * 8, 'Lista de Compras', '-' * 8)

    try:
        escolha = int(input("Selecione uma opção\n[1]inserir [2]excluir [3]listar: "))

        if escolha == 1:
            valor = input("Item: ")
            lista_compra.append(valor)

        elif escolha == 2:
            for i in range(len(lista_compra)):
                print(i, lista_compra[i])
            posicao = int(input("Digite a posição do item que quer excluir: "))

            try:
                del lista_compra[posicao]
            except IndexError:
                print("\nPosição da lista inválido!\n")

        elif escolha == 3:
            for i in range(len(lista_compra)):
                print(i, lista_compra[i])

    except ValueError:
        print("\nDigite apenas valores inteiros!\n")
