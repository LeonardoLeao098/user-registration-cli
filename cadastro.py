import json
import os
import getpass

ARQUIVO = 'dados.json'

def carregar_dados():
    if not os.path.isfile(ARQUIVO):
        return []
    with open(ARQUIVO, 'r') as f:
        return json.load(f)

def salvar_dados(lista):
    with open(ARQUIVO, 'w') as f:
        json.dump(lista, f, indent=4)

def cadastrar_pessoa():
    print("\n--- Novo Cadastro ---")
    pessoa = {}
    pessoa['nome'] = input("Nome: ")

    while True:
        cpf = input("CPF: ")
        if cpf.isdigit():
            pessoa['cpf'] = int(cpf)
            break
        else:
            print("Digite apenas números para o CPF.")

    pessoa['email'] = input("Email: ")
    pessoa['endereco'] = input("Endereço: ")

    while True:
        idade = input("Idade: ")
        if idade.isdigit():
            pessoa['idade'] = int(idade)
            break
        else:
            print("Digite apenas números para a idade.")

    while True:
        try:
            nota1 = float(input("Nota 1: "))
            if 0 <= nota1 <= 10:
                pessoa['nota1'] = nota1
                break
            else:
                print("Digite uma nota entre 0 e 10.")
        except:
            print("Digite um número válido.")

    while True:
        try:
            nota2 = float(input("Nota 2: "))
            if 0 <= nota2 <= 10:
                pessoa['nota2'] = nota2
                break
            else:
                print("Digite uma nota entre 0 e 10.")
        except:
            print("Digite um número válido.")

    while True:
        try:
            trabalho = float(input("trabalho: "))
            if 0 <= trabalho <= 10:
                pessoa['trabalho'] = trabalho
                break
            else:
                print("Digite uma nota entre 0 e 10.")
        except:
            print("Digite um número válido.")

    while True:
        senha = getpass.getpass("Crie uma senha (mínimo 8 caracteres): ").strip()
        if len(senha) >= 8:
            pessoa['senha'] = senha
            break
        else: 
            print("A senha deve ter no mínimo 8 caracteres. Tente novamente: ")
            
    print("\n>> Declaração:")
    print("Eu reconheço que meus dados serão utilizados apenas para fins educacionais e não serão compartilhados.")
    confirmacao = input("Digite 'sim' para confirmar: ").strip().lower()

    if confirmacao == 'sim':
        dados = carregar_dados()
        dados.append(pessoa)
        salvar_dados(dados)
        print(">> Cadastro realizado com sucesso!")
    else:
        print("Cadastro cancelado. Você não confirmou o uso dos dados.")

def listar_pessoas():
    dados = carregar_dados()
    if len(dados) == 0:
        print("\nNenhum dado encontrado.")
        return

    print("\n--- Lista de Cadastros ---")
    for i, pessoa in enumerate(dados, 1):
        print(f"\nPessoa {i}")
        print(f"Nome: {pessoa.get('nome', 'Sem dados')}")
        print(f"CPF: {pessoa.get('cpf', 'Sem dados')}")
        print(f"Email: {pessoa.get('email', 'Sem dados')}")
        print(f"Endereço: {pessoa.get('endereco', 'Sem dados')}")
        print(f"Idade: {pessoa.get('idade', 'Sem dados')}")
        print(f"Nota 1: {pessoa.get('nota1', 'Sem dados')}")
        print(f"Nota 2: {pessoa.get('nota2', 'Sem dados')}")
        print(f"Trabalho: {pessoa.get('trabalho', 'Sem dados')}")

def alterar_cadastro():
    dados = carregar_dados()
    if not dados:
        print("\nNão há cadastros ainda.")
        return

    alvo = input("\nDigite o CPF da pessoa que quer alterar: ")
    for pessoa in dados:
        if pessoa['cpf'] == alvo:
            senha = input("Digite a senha do cadastro: ").strip()
            if senha != pessoa.get('senha'):
                print("Senha incorreta. Alteração não permitida.")
                return

            print("Cadastro encontrado. Deixe em branco se quiser manter o valor atual.")

            novo_nome = input(f"Nome ({pessoa['nome']}): ")
            novo_email = input(f"Email ({pessoa['email']}): ")
            novo_endereco = input(f"Endereço ({pessoa['endereco']}): ")
            nova_idade = input(f"Idade ({pessoa['idade']}): ")
            nova_nota1 = input(f"Nota 1 ({pessoa['nota1']}): ")
            nova_nota2 = input(f"Nota 2 ({pessoa['nota2']}): ")
            novo_trabalho = input(f"Trabalho ({pessoa['trabalho']}): ")

            if novo_nome:
                pessoa['nome'] = novo_nome
            if novo_email:
                pessoa['email'] = novo_email
            if novo_endereco:
                pessoa['endereco'] = novo_endereco
            if nova_idade:
                pessoa['idade'] = nova_idade
            if nova_nota1:
                pessoa['nota1'] = nova_nota1
            if nova_nota2:
                pessoa['nota2'] = nova_nota2
            if novo_trabalho:
                pessoa['trabalho'] = novo_trabalho

            salvar_dados(dados)
            print(">> Dados atualizados com sucesso!")
            return

    print("CPF não encontrado.")

def encerrar():
    os.system('cls')
    print('Encerrando...')

def menu():
    while True:
        try:
            print("\n==== MENU ====")
            print("1. Cadastrar")
            print("2. Listar")
            print("3. Alterar")
            print("4. Sair")

            escolha = int(input("Opção: "))

            if escolha == 1:
                cadastrar_pessoa()
            elif escolha == 2:
                listar_pessoas()
            elif escolha == 3:
                alterar_cadastro()
            elif escolha == 4:
                encerrar()
                break
            else:
                print("Opção inválida, tente de novo.")
        except:
            print('Entrada inválida!')
menu()
