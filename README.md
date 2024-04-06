# AWS Cognito Flask Authentication

Este projeto é uma aplicação Flask Python que utiliza o AWS Cognito para autenticar usuários. Permite o cadastro de novos usuários, login e validação de token de acesso.

## Recursos Utilizados

- **Python 3.8+**: Linguagem de programação.
- **Flask**: Framework web para Python.
- **Boto3**: SDK da AWS para Python, usado para interagir com o AWS Cognito.
- **python-dotenv**: Biblioteca para carregar variáveis de ambiente a partir de um arquivo `.env`.

## Configuração Inicial

### Pré-Requisitos

Certifique-se de ter o Python 3.8+ instalado em seu sistema. Além disso, você precisará de uma conta na AWS e um pool de usuários configurado no AWS Cognito.

### Instalação

1. Clone o repositório para a sua máquina local:
   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:
   ```plaintext
   COGNITO_USER_POOL_ID=<seu-user-pool-id>
   COGNITO_CLIENT_ID=<seu-client-id>
   REGION_NAME=<sua-regiao>
   ```

### Execução

Para iniciar a aplicação, execute:

```bash
flask run
```

A aplicação estará acessível em `http://localhost:5000`.

## Endpoints Disponíveis

- `POST /signup`: Registra um novo usuário.
  - Payload: `{ "username": "nomeusuario", "password": "senha" }`

- `POST /signin`: Realiza o login.
  - Payload: `{ "username": "nomeusuario", "password": "senha" }`
  
- `POST /validate`: Valida o token de acesso.
  - Headers: `Authorization: <token>`

## Contribuições

Contribuições são sempre bem-vindas! Por favor, crie um fork do repositório e faça um pull request com suas mudanças, ou abra uma issue com detalhes sobre o que você gostaria de mudar ou adicionar.

## Licença

[MIT](LICENSE)
