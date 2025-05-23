# Controle de estoque Complexo
import json
import os

while True:
    print('\n=== CONTROLE DE ESTOQUE - PUB ===')
    print('1. Cadastrar novo produto')
    print("2. Registrar entrada de produto")
    print('3. Registrar saída de produto')
    print('4. Consultar estoque')
    print('5. Sair')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        nome = input('Nome do produto: ')
        categoria = input('Qual a categoria (bebida, comida, suprimentos): ')
        quantidade = int(input('Quantidade inicial: '))

        produto = {
            'Nome' : nome,
            'Categoria' : categoria,
            'Quantidade' : quantidade
            }
        print(produto)
        if os.path.exists('estoque.json'):
            with open('estoque.json', 'r') as arquivo:
                estoque = json.load(arquivo)
        else:
            estoque = {}
            novo_id = str(len(estoque) + 1)
            estoque[novo_id] = produto
            with open('estoque.json', 'w') as arquivo:
                json.dump(estoque, arquivo, indent=4)
            print("Produto cadastrado com sucesso!")
    elif opcao == '2':
            # 1. Verifica se o arquivo existe
        if os.path.exists('estoque.json'):
            with open('estoque.json', 'r') as arquivo:
                estoque = json.load(arquivo)
        else:
            print("Nenhum produto cadastrado ainda.")
            continue  # volta para o menu

        # 2. Mostra os produtos cadastrados
        print("\nProdutos cadastrados:")
        for id, dados in estoque.items():
            print(f"{id} - {dados['Nome']} ({dados['Quantidade']} unidades)")

        # 3. Pede o ID do produto
        id_produto = input("\nDigite o ID do produto que recebeu entrada: ")

        if id_produto not in estoque:
            print("ID inválido.")
            continue

        # 4. Pede a quantidade a adicionar
        entrada = int(input("Quantidade a adicionar: "))

        # 5. Atualiza o valor
        estoque[id_produto]['Quantidade'] += entrada

        # 6. Salva de volta no arquivo
        with open('estoque.json', 'w') as arquivo:
            json.dump(estoque, arquivo, indent=4)

        print("Entrada registrada com sucesso!")

    elif opcao == '3':
        input('Registrar a saída do produto')
    elif opcao == '4':
        print('Consulta de estoque')
    elif opcao == '5':
        print("Saindo do sistema...")
        break
    else: 
        print('Opção inválida. Tente novamente!')
