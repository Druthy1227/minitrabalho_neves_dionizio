# Luiz Gustavo Santos Neves e Guilherme Dionizio de Lima | 2025B010956 e 2025b011319
# Tema: Agenda de Contatos (refatoração de estruturado para POO)


class Categoria:
    """Classe associada: representa o grupo ao qual o contato pertence."""

    def __init__(self, nome):
        self.nome = nome.strip().lower()  # normaliza para minúsculas e sem espaços

    def __str__(self):
        return self.nome


class Contato:
    """Classe de domínio principal."""

    _proximo_id = 1  # gera IDs automaticamente

    def __init__(self, nome, telefone, email, categoria):
        self.__id = Contato._proximo_id
        Contato._proximo_id += 1

        self.nome = nome
        self.__telefone = telefone
        self.__email = ""
        self.set_email(email)          # passa pela validação já na criação
        self.categoria = categoria     # ASSOCIAÇÃO: guarda um objeto Categoria

    # --- encapsulamento: id (somente leitura) ---
    def get_id(self):
        return self.__id

    # --- encapsulamento: telefone ---
    def get_telefone(self):
        return self.__telefone

    def set_telefone(self, valor):
        self.__telefone = valor

    # --- encapsulamento: email, COM validação ---
    def get_email(self):
        return self.__email

    def set_email(self, valor):
        if "@" not in valor or "." not in valor.split("@")[-1]:
            print(f"\nE-mail '{valor}' inválido. E-mail não foi cadastrado/alterado.")
            return False
        self.__email = valor

    def __str__(self):
        return (f"[{self.__id}] {self.nome:<20} | Tel: {self.__telefone:<15} "
                f"| Email: {self.__email:<25} | Categoria: {self.categoria}")

# HERANÇA: um ContatoProfissional É UM Contato, com dados extras de trabalho.
class ContatoProfissional(Contato):


    def __init__(self, nome, telefone, email, categoria, empresa, cargo):
        super().__init__(nome, telefone, email, categoria)
        self.empresa = empresa
        self.cargo = cargo

    def __str__(self):  # SOBRESCRITA usando super()
        base = super().__str__()
        return base + f" | Empresa: {self.empresa} ({self.cargo})"

# Classe gerenciadora: guarda a coleção e centraliza as operações.
class Agenda:
    

    def __init__(self):
        self.__contatos = []  # coleção privada

    def cadastrar(self, contato):
        if not isinstance(contato, Contato):
            print("Só é possível cadastrar objetos do tipo Contato.")
            return
        self.__contatos.append(contato)
        print(f"'{contato.nome}' cadastrado com sucesso!")

    def listar(self):
        if not self.__contatos:
            print("A agenda está vazia.")
            return
        print("\n===== CONTATOS =====")
        for c in self.__contatos:
            print(c)

    def buscar(self, id_busca):
        for c in self.__contatos:
            if c.get_id() == id_busca:
                return c
        return None

    def remover(self, id_busca):
        contato = self.buscar(id_busca)
        if contato is None:
            print("Contato não encontrado.")
            return
        self.__contatos.remove(contato)
        print(f"'{contato.nome}' removido com sucesso!")

    def relatorio(self):
        total = len(self.__contatos)
        print("\n===== RELATÓRIO =====")
        if total == 0:
            print("A agenda está vazia no momento.")
            return

        print(f"Total de contatos: {total}")

        contagem_categorias = {}
        for c in self.__contatos:
            nome_cat = str(c.categoria)
            contagem_categorias[nome_cat] = contagem_categorias.get(nome_cat, 0) + 1

        for cat, qtd in contagem_categorias.items():
            print(f"  {cat}: {qtd}")

        profissionais = sum(1 for c in self.__contatos if isinstance(c, ContatoProfissional))
        print(f"Contatos profissionais: {profissionais}")

        # Encontra a categoria com a maior quantidade de contatos
        maior_quantidade = 0
        maior_categoria = ""
        
        for cat, qtd in contagem_categorias.items():
            if qtd > maior_quantidade:
                maior_quantidade = qtd 
                maior_categoria = cat  

        print(f"\nCategoria principal: {maior_categoria} ({maior_quantidade} registros)")


def exibir_menu():
    print("\n===== AGENDA DE CONTATOS (OO) =====")
    print("1 - Cadastrar contato comum")
    print("2 - Cadastrar contato profissional")
    print("3 - Listar")
    print("4 - Buscar")
    print("5 - Alterar dados")
    print("6 - Remover")
    print("7 - Relatório")
    print("0 - Sair")


def main():
    agenda = Agenda()

    # categorias fixas de exemplo, como Categoria em Produto->Categoria
    cat_amigo = Categoria("Amigo")
    cat_trabalho = Categoria("Trabalho")

    # dados iniciais, equivalentes aos dois registros da Parte 1
    agenda.cadastrar(Contato("Luiz", "82 12345-7890", "teste1@gmail.com", cat_amigo))
    agenda.cadastrar(ContatoProfissional(
        "Guilherme", "82 12345-7891", "teste2@gmail.com", cat_trabalho,
        "UNI-RN", "Estudante"
    ))

    while True:
        exibir_menu()
        opcao = input("Opção: ").strip()

        if opcao == "1":
            nome = input("Nome: ")
            tel = input("Telefone: ")
            email = input("Email: ")
            nome_cat = input("Categoria: ")
            agenda.cadastrar(Contato(nome, tel, email, Categoria(nome_cat)))

        elif opcao == "2":
            nome = input("Nome: ")
            tel = input("Telefone: ")
            email = input("Email: ")
            nome_cat = input("Categoria: ")
            empresa = input("Empresa: ")
            cargo = input("Cargo: ")
            agenda.cadastrar(ContatoProfissional(
                nome, tel, email, Categoria(nome_cat), empresa, cargo
            ))

        elif opcao == "3":
            agenda.listar()

        elif opcao == "4":
            try:
                id_busca = int(input("ID a buscar: "))
            except ValueError:
                print("ID inválido.")
                continue
            achado = agenda.buscar(id_busca)
            print(achado if achado else "Contato não encontrado.")

        elif opcao == "5":
            try:
                id_busca = int(input("ID a alterar: "))
            except ValueError:
                print("ID inválido.")
                continue
            
            # 1. Buscar ANTES do laço para evitar o UnboundLocalError
            contato = agenda.buscar(id_busca)
            if contato is None:
                print("Contato não encontrado.")
                continue

            while True:
                print(f"\n--- Editando contato: {contato.nome} ---")
                print("1 - Alterar nome")
                print("2 - Alterar telefone")
                print("3 - Alterar email")
                print("4 - Alterar categoria")
                
                # Exibe opções extras se for profissional
                if isinstance(contato, ContatoProfissional):
                    print("5 - Alterar empresa")
                    print("6 - Alterar cargo")
                
                print("0 - Voltar ao menu principal")
                sub_opcao = input("Escolha uma opção: ").strip()

                if sub_opcao == "1":
                    novo_nome = input("Novo nome: ").strip()
                    if novo_nome:
                        contato.nome = novo_nome
                        print("Nome atualizado!")
                elif sub_opcao == "2":
                    novo_tel = input("Novo telefone: ").strip()
                    if novo_tel:
                        contato.set_telefone(novo_tel)
                        print("Telefone atualizado!")
                elif sub_opcao == "3":
                    novo_email = input("Novo email: ").strip()
                    if novo_email:
                        contato.set_email(novo_email)
                        print("Email processado!")
                elif sub_opcao == "4":
                    nova_cat = input("Nova categoria: ")
                    if nova_cat:
                        contato.categoria = Categoria(nova_cat) 
                        print("Categoria atualizada!")
                elif sub_opcao == "5" and isinstance(contato, ContatoProfissional):
                    nova_empresa = input("Nova empresa: ").strip()
                    if nova_empresa:
                        contato.empresa = nova_empresa
                        print("Empresa atualizada!")
                elif sub_opcao == "6" and isinstance(contato, ContatoProfissional):
                    novo_cargo = input("Novo cargo: ").strip()
                    if novo_cargo:
                        contato.cargo = novo_cargo
                        print("Cargo atualizado!")
                elif sub_opcao == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "6":
            try:
                id_busca = int(input("ID a remover: "))
            except ValueError:
                print("ID inválido.")
                continue
            
            contato = agenda.buscar(id_busca)
            
            if contato is None:
                print("Contato não encontrado.")
                continue
        
            print("\nRegistro selecionado:")
            print(contato)
            confirmacao = input(f"\nRealmente deseja remover o usuário {contato.nome}? (y/n): ").strip().lower()
            
            if confirmacao == 'y':
                agenda.remover(id_busca)
            else:
                print("Operação cancelada.")


if __name__ == "__main__":
    main()