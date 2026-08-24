registro = [
    {"id": 1, "nome": "Luiz", "telefone": "82 12345-7890", "email": "teste1@gmail.com", "categoria": "estudante"},
    {"id": 2, "nome": "Guilherme", "telefone": "82 12345-7891", "email": "teste2@gmail.com", "categoria": "estudante"},
 ] # nosso "banco de dados" em memoria

def exibir_menu():
    print("\n===== SISTEMA DE CADASTRO =====")
    print("1 - Cadastrar 2 - Listar 3 - Buscar")
    print("4 - Alterar 5 - Remover 6 - Relatorio")

def cadastrar(lista):
    novo_usuario = {}
    novo_usuario["id"] = len(registro) + 1
    novo_usuario["nome"] = input("Insira o nome a ser cadastrado: ")
    novo_usuario["telefone"] = input("Insira o telefone a ser cadastrado: ")
    novo_usuario["email"] = input("Insira o email a ser cadastrado: ")
    novo_usuario["categoria"] = input("Insira a categoria a ser cadastrada: ")
    lista.append(novo_usuario)

def listar(lista):
    for i in lista:
        print("-" * 88)
        print(f"{i['id']:<5} | {i['nome']:<20} | {i['telefone']:<15} | {i['email']:<25} | {i['categoria']:<15}")


def buscar(lista):
    id_busca = int(input("Digite o ID a procurar: "))

    for usuario in lista:
        if usuario["id"] == id_busca:
            print("\nRegistro encontrado:")
            print("-" * 88)
            print(f"{usuario['id']:<5} | {usuario['nome']:<20} | {usuario['telefone']:<15} | {usuario['email']:<25} | {usuario['categoria']:<15}")
            return usuario

def alterar(lista):
    id_busca = int(input("Digite o ID do usuário: "))

    for usuario in lista:
        if usuario["id"] == id_busca:

            print(f"Nome atual: {usuario['nome']}")
            novo_nome = input("Novo nome: ")

            if novo_nome.strip():
                usuario["nome"] = novo_nome

            print("Registro atualizado!")
            return

    print("Registro não encontrado.")

def remover(lista):
    print("===== REMOVER REGISTRO =====")

    usuario_encontrado = buscar(lista)

    if usuario_encontrado:
        confirmacao = input(f"\n Realmente deseja remover o usuário {usuario_encontrado['nome']}? (y/n): ").strip().lower()

        if confirmacao == 'y':
            lista.remove(usuario_encontrado)
            print("Registro removido com sucesso!")
        else:
            print("Operação cancelada.")

def relatorio(lista):
    total = len(lista)

    print("\n===== RELATÓRIO =====")
    print(f"Total de registros: {total}")
    print(f"Maior ID registrado: {max(usuario['id'] for usuario in lista) if lista else 'N/A'}")

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
