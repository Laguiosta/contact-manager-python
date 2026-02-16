import os
import time

lista_de_contatos = []


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


def pausa():
    input("\nPressione ENTER para continuar...")


def exibir_opcoes():
    print("\n1. Cadastrar contato")
    print("2. Ver contatos")
    print("3. Favoritar contato")
    print("4. Editar contato")
    print("5. Ver favoritos")
    print("6. Deletar contato")
    print("7. Sair")


def pedir_indice(lista):
    try:
        indice = int(input("Digite o índice do contato: ")) - 1
        if 0 <= indice < len(lista):
            return indice
        else:
            print("Índice inválido.")
            time.sleep(1)
            return None
    except ValueError:
        print("Digite apenas números.")
        time.sleep(1)
        return None


def cadastrar_contato(lista):
    limpar()

    nome = input("Nome: ")
    telefone = input("Telefone: ")

    email = None
    escolha = input("Deseja adicionar email? [S/N] ").strip().lower()

    if escolha.startswith("s"):
        email = input("Email: ")

    lista.append({
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "favorito": False
    })

    print("\nContato cadastrado com sucesso!")
    time.sleep(1)


def ver_contatos(lista):
    limpar()

    if not lista:
        print("Nenhum contato cadastrado.")
        return

    for i, contato in enumerate(lista, start=1):
        status = "★" if contato["favorito"] else " "
        print(f"{i}. {status} {contato['nome']}")
        print(f"   Tel: {contato['telefone']}")
        print(f"   Email: {contato['email'] or 'Não cadastrado'}\n")


def favoritar_contato(lista):
    ver_contatos(lista)

    if not lista:
        return

    indice = pedir_indice(lista)
    if indice is None:
        return

    lista[indice]["favorito"] = not lista[indice]["favorito"]

    print("Status alterado com sucesso!")
    time.sleep(1)


def editar_contato(lista):
    ver_contatos(lista)

    if not lista:
        return

    indice = pedir_indice(lista)
    if indice is None:
        return

    while True:
        escolha = input("Editar (N)ome, (T)elefone ou (E)mail? ").lower()

        if escolha.startswith("n"):
            lista[indice]["nome"] = input("Novo nome: ")
            break

        elif escolha.startswith("t"):
            lista[indice]["telefone"] = input("Novo telefone: ")
            break

        elif escolha.startswith("e"):
            lista[indice]["email"] = input("Novo email: ")
            break

        else:
            print("Opção inválida.")


def visualizar_favoritos(lista):
    limpar()

    favoritos = [c for c in lista if c["favorito"]]

    if not favoritos:
        print("Nenhum favorito.")
        return

    for i, contato in enumerate(favoritos, start=1):
        print(f"{i}. {contato['nome']}")
        print(f"   Tel: {contato['telefone']}")
        print(f"   Email: {contato['email'] or 'Não cadastrado'}\n")


def deletar_contato(lista):
    ver_contatos(lista)

    if not lista:
        return

    indice = pedir_indice(lista)
    if indice is None:
        return

    removido = lista.pop(indice)
    print(f"{removido['nome']} removido com sucesso!")
    time.sleep(1)


# LOOP PRINCIPAL
while True:
    limpar()
    exibir_opcoes()

    try:
        escolha = int(input("\nEscolha: "))
    except ValueError:
        print("Digite um número válido.")
        time.sleep(1)
        continue

    if escolha == 1:
        cadastrar_contato(lista_de_contatos)

    elif escolha == 2:
        ver_contatos(lista_de_contatos)
        pausa()

    elif escolha == 3:
        favoritar_contato(lista_de_contatos)

    elif escolha == 4:
        editar_contato(lista_de_contatos)

    elif escolha == 5:
        visualizar_favoritos(lista_de_contatos)
        pausa()

    elif escolha == 6:
        deletar_contato(lista_de_contatos)

    elif escolha == 7:
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")
        time.sleep(1)
