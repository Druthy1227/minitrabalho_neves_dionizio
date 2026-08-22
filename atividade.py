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
    novo_usuario["id"] = len(registro) + 1
    novo_usuario["nome"] = input("Insira o nome a ser cadastrado: ")
    novo_usuario["telefone"] = input("Insira o telefone a ser cadastrado: ")
    novo_usuario["email"] = input("Insira o email a ser cadastrado: ")
    novo_usuario["categoria"] = input("Insira a categoria a ser cadastrada: ")
    lista.append(novo_usuario)

def listar(lista):
    for i in lista:
        print(f"{i['id']} {i['nome']}")


def buscar(lista): 
    ...

def alterar(lista): 
    ...

def remover(lista):
    confirmacao = input("Realmente deseja remover um usuário? y/n")
    if confirmacao == "y":
        registro.remove(input("Insira o id do registro a ser removido: "))

def relatorio(lista): 
    ...

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
