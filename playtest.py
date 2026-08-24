# Luiz Gustavo Santos Neves e Guilherme Dionizio de Lima | 2025B010956 e 2025b011319 |  Tema escolhido: Agenda de Contatos

registro = [
    {"id": 1, "nome": "Luiz", "telefone": "82 12345-7890", "email": "teste1@gmail.com", "categoria": "estudante"},
    {"id": 2, "nome": "Guilherme", "telefone": "82 12345-7891", "email": "teste2@gmail.com", "categoria": "estudante"},
 ] # nosso "banco de dados" em memoria

def exibir_menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar 2 - Listar 3 - Buscar")
    print("4 - Alterar 5 - Remover 6 - Relatorio")
    print("0 - Sair")

def cadastrar(lista):
    novo_usuario = {}
    novo_usuario["id"] = max([u['id'] for u in lista], default=0) + 1
    novo_usuario["nome"] = input("Insira o nome a ser cadastrado: ")
    novo_usuario["telefone"] = input("Insira o telefone a ser cadastrado: ")
    novo_usuario["email"] = input("Insira o email a ser cadastrado: ")
    novo_usuario["categoria"] = input("Insira a categoria a ser cadastrada: ").strip().lower()
    lista.append(novo_usuario)

def listar(lista):
    print(f"{'ID':<5} | {'Nome':<20} | {'Telefone':<15} | {'Email':<25} | {'Categoria':<15}")
    for i in lista:
        print("-" * 88)
        print(f"{i['id']:<5} | {i['nome']:<20} | {i['telefone']:<15} | {i['email']:<25} | {i['categoria']:<15}")


def buscar(lista):
    try:
        id_busca = int(input("Digite o ID a procurar: "))
    except ValueError:
        print("ID inválido. Por favor, digite um número.")
        return None
    for usuario in lista:
        if usuario["id"] == id_busca:
            print("\nRegistro encontrado:")
            print("-" * 88)
            print(f"{usuario['id']:<5} | {usuario['nome']:<20} | {usuario['telefone']:<15} | {usuario['email']:<25} | {usuario['categoria']:<15}")
            return usuario

    print("Registro não encontrado.")
    return None

def alterar(lista):
    id_busca = buscar(lista)

    if id_busca:
            while True:
                print(f"\n--- Editando contato: {id_busca['nome']} ---")
                print("1 - Alterar Nome")
                print("2 - Alterar Telefone")
                print("3 - Alterar Email")
                print("4 - Alterar Categoria")
                print("0 - Voltar ao menu principal")

                opcao = input("Escolha uma opção: ").strip()

                if opcao == "1":
                    id_busca["nome"] = input("Novo nome: ")
                elif opcao == "2":
                    id_busca["telefone"] = input("Novo telefone: ")
                elif opcao == "3":
                    id_busca["email"] = input("Novo email: ")
                elif opcao == "4":
                    id_busca["categoria"] = input("Nova categoria: ").strip().lower()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")


def remover(lista):
    print("===== REMOVER REGISTRO =====")

    id_busca = buscar(lista)

    if id_busca:
        confirmacao = input(f"\n Realmente deseja remover o usuário {id_busca['nome']}? (y/n): ").strip().lower()

        if confirmacao == 'y':
            lista.remove(id_busca)
            print("Registro removido com sucesso!")
        else:
            print("Operação cancelada.")

def relatorio(lista):
    total = len(lista)
    print("\n===== RELATÓRIO =====")
    
    if total == 0:
        print("O sistema está vazio no momento.")
        return

    print(f"Total de registros: {total}\n")

    contagem_categorias = {} # Dicionário de Categorias
    for usuario in lista:
        cat = usuario['categoria']
        contagem_categorias[cat] = contagem_categorias.get(cat, 0) + 1 
        # .get(valor, valor_padrao) -> retorna o valor da chave se existir, caso contrário retorna o valor padrão para somar

    for cat, qtd in contagem_categorias.items():
        print(f"Total de {cat}: {qtd}")

    maior_quantidade = 0
    maior_categoria = ""
    
    for cat, qtd in contagem_categorias.items():
        if qtd > maior_quantidade:
            maior_quantidade = qtd
            maior_categoria = cat

    print(f"\nCategoria principal: {maior_categoria} ({maior_quantidade} registros)")


def main():  # funcao principal
    while True:
        exibir_menu()
        opcao = input("Opcao: ").strip()
        if opcao == "1": 
            cadastrar(registro)
        elif opcao == "2": 
            listar(registro)
        elif opcao == "3": 
            buscar(registro)
        elif opcao == "4": 
            alterar(registro)
        elif opcao == "5": 
            remover(registro)
        elif opcao == "6": 
            relatorio(registro)
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida. Tente novamente.")

main()
