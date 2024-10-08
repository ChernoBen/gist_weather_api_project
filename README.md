# Gist Weather API

API integrada com serviço de clima para publicação de comentários em um Gist específico.

## Rotas
- **GET**: `/docs` - Acesso à página do Swagger.
- **POST**: `/gist` - Publica um comentário em um Gist.

## Inicializando o Projeto

### Via Docker
1. Certifique-se de que o Docker esteja instalado e atualizado em sua máquina.
2. Execute o comando:
   ```bash
   docker compose up


## Testes

Os testes podem ser executados tanto em um ambiente Docker quanto localmente. Abaixo estão as instruções para ambas as opções.

### Testes via Docker

1. **Pré-requisitos**: Certifique-se de que o Docker esteja instalado e atualizado em sua máquina.
2. **Executando os testes**: Use o seguinte comando para rodar os testes:
   ```bash
   docker compose run tests

## Dependência: PyGithub

- **PyGithub==2.4.0**: Esta biblioteca fornece uma interface fácil de usar para interagir com a API do GitHub. Com o PyGithub, é possível realizar operações como:

  - **Autenticação**: Permite a autenticação usando tokens de acesso, facilitando a interação com repositórios privados e operações sensíveis.
  - **Gerenciamento de Repositórios**: Criação, edição, exclusão e consulta de repositórios no GitHub.
  - **Manipulação de Gists**: Permite publicar, editar e excluir gists, além de acessar informações sobre gists existentes.
  - **Gerenciamento de Issues e Pull Requests**: Criação, edição e consulta de issues e pull requests em repositórios, facilitando a colaboração em projetos.
  - **Acesso a Dados de Usuários**: Consulta a informações sobre usuários, organizações e repositórios públicos.

### Utilização no Projeto

A dependência `PyGithub` é fundamental para a funcionalidade de nossa API, permitindo que os usuários publiquem comentários em gists de forma programática. Por meio dessa biblioteca, nossa aplicação consegue interagir diretamente com a plataforma GitHub, oferecendo uma interface robusta e flexível para gerenciar comentários e gists.


