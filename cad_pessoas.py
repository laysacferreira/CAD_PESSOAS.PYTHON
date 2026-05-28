import os

opcao = 0

while (opcao != 3):
    print("------ MENU -----")
    print("1 - para cadastrar")
    print("2 - para listar")
    print("3 - para sair")
 
    opcao = int(input("escolha a opção: "))
 
    if opcao == 1:
        print("cadastrar pessoas")
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu E-mail: ")

        arquivo = open("pessoas.txt", "a")
        arquivo.write(f"{nome},{telefone},{email}\n")
        arquivo.close()
       
 
        print("Usuário cadastrado com sucesso")
        input()
        os.system("cls")
    elif (opcao == 2):
        print("listar pessoas")

        arquivo = open("pessoas.txt", "r")

        for linha in arquivo:
            nome, telefone , email = linha.strip().split(",")
            print(f"Nome da pessoa: {nome}")
            print(f"Telefone da pessoa: {telefone}")
            print(f"Email da pessoa: {email}")
            print("-----------------------------")
        arquivo.close()
        input()
        os.system("cls")