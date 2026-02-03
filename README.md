# Sistema de Cadastro em Terminal (Python)

Aplicação em Python executada no terminal (CLI) para cadastro, listagem e alteração de dados de pessoas, com persistência em arquivo JSON e proteção por senha.

## Funcionalidades
- Cadastrar pessoas com dados pessoais e notas
- Armazenar os dados em arquivo JSON
- Listar todos os cadastros salvos
- Alterar um cadastro existente utilizando CPF e senha
- Validação de senha com entrada oculta (`getpass`)
- Menu interativo no terminal

## Dados armazenados
Cada cadastro contém:
- Nome
- CPF
- Email
- Endereço
- Idade
- Notas (nota 1, nota 2 e trabalho)
- Senha (armazenada para fins educacionais)

Os dados são salvos localmente no arquivo `dados.json`.

## Segurança e observações

- As senhas são utilizadas apenas para fins educacionais
- Os dados não são criptografados
- Este projeto não deve ser usado em produção
- O foco é prática de lógica, organização e persistência de dados

## O que eu aprendi com esse projeto

- Manipulação de arquivos JSON
- Persistência de dados em Python
- Organização de funções
- Criação de menus interativos no terminal
- Validação de entradas do usuário
- Controle de acesso com senha
- Boas práticas em projetos de linha de comando (CLI)
