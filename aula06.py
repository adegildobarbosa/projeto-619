banco_de_dados =[
    {
        "codigo": 1,
        "nome": "mouse",
        "preco":  150.50,
        "disponivel": True

    }
]
codigo_atual = 1


def cadastrar_produtos(nome: str, preco : float) -> None:
    global codigo_atual
    codigo_atual += 1
    produtos = {
        "codigo": codigo_atual,
        "nome" : nome,
        "preco" : preco,
        "disponivel": True
    }
    banco_de_dados.append(produtos)
    print('produto adicionado com sucesso!')
cadastrar_produtos("fone de ouvido", 59.99)
print(banco_de_dados)

def listar_produtos():
    print('--- PRODUTOS CADASTRAR---')
    for produtos in banco_de_dados:
        # produtos
        print(f"código:{produtos['codigo']}")
        print(f"nome:{produtos['nome']}")
        print(f"preco:{produtos['preco']}")
        print(f"disponivel:{produtos['disponivel']}")
        print('-'*50)

cadastrar_produtos("fone de ouvido", 59.99)
listar_produtos()
def buscar_produto(codigo : int):
    for produto in banco_de_dados:
        if produto['codigo'] == codigo:
            return produto
    return None

def deletar_produto(codigo: int):
    produto = buscar_produto(codigo)
    if produto:
        banco_de_dados.remove(produto)
        print('produto removido com sucesso!')
        return
    print('produto não encontrado!')

cadastrar_produtos("fone de ouvido", 59.99)
listar_produtos()
deletar_produto(1)
print(banco_de_dados)
deletar_produto(-1)
# print(buscar_produto(1))
# print(buscar_produto(.1))
def editar_produto(codigo: int, nome: str, preco: float):
    produto = buscar_produto(codigo)
    if produto:
        produto['nome'] = nome
        produto['preco'] = preco
        print('dados alterados com sucesso!')
        return
    print('produto não encontrado!')

cadastrar_produtos("fone de ouvido", 59.99)
editar_produto(1, "Processador", 899.99)
listar_produtos()
editar_produto(-1, "fone ", 500)

def menu():
    print('--- BEM VINDO AO MENU---')   
    while True:
        print('1,-Adicionar produto')
        print('2, - Editar produto')
        print('3,- listar produto')
        print('4 - deletar produto')
        print('0,- sair')

        opcao = input('selecione uma opcao')
        if opcao == '1':
            nome = input('digite o nome do produto')
            preco = float(input('digite o preco do produto:'))
            cadastrar_produtos(nome, preco)
        elif opcao == '2':
            codigo = int(input('digite o codigo do produto'))
            nome = input('digiteo nome do produto:')
            preco = float(input('digite o preco do produto:'))
            editar_produto(codigo,nome , preco)
        elif opcao =='3':
            listar_produtos()
        elif opcao =='4':
            codigo = int(input('digite o codigo do produto:'))
            print(buscar_produtos(codigo))
        elif opcao == '5':
            codigo= int(input('digiteo codigo do produto:'))
            deletar_produto(codigo)
        elif  opcao == '0':
            print('você saiu do programa!')
            break
        else:
            print('opcao invalida')

menu()