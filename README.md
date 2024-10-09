# Gist Weather API

API integrada com serviço de clima para publicação de comentários em um Gist específico.

## Rotas
- **GET**: `/docs` - Acesso à página do Swagger.
- **POST**: `/gist` - Publica um comentário em um Gist.

## Inicializando o Projeto

### Via Docker
1. Certifique-se de que o Docker esteja instalado e atualizado em sua máquina.
2. Certifique-se de definir as variáveis de ambiente no seu `.env` conforme o arquivo `.env.example`
3. Execute o comando:
   ```bash
   docker compose up
4. Siga para o caminho `127.0.0.1:8080/docs`
5. Execute a `/gist` conforme o exemplo abaixo :
   ```
   {
      "city": "Sao Paulo",
      "country": "br"
   }
6. Em caso de sucesso, é esperado uma resposta contendo a url para o gist que deseja inserir o comentário conforme exemplo abaixo:
   ```
   {
      "url": "https://gist.github.com/ChernoBen/c8beda72087bfc659e92915922aa28ec"   
   }

## Testes

Os testes podem ser executados tanto em um ambiente Docker quanto localmente. Abaixo estão as instruções para ambas as opções.

### Testes via Docker

1. **Pré-requisitos**: Certifique-se de que o Docker esteja instalado e atualizado em sua máquina.
2. **Executando os testes**: Use o seguinte comando para rodar os testes:
   ```bash
   docker compose run tests

### Principais dependências:

## Dependência: Weather SDK

- **Weather SDK**: Esta biblioteca oferece uma interface para interagir com serviços de clima, permitindo que desenvolvedores integrem funcionalidades de previsão do tempo em suas aplicações. A dependência pode incluir serviços como OpenWeatherMap, WeatherAPI, ou outros serviços de clima populares.

### Principais Funcionalidades

1. **Consulta de Dados Meteorológicos**: Permite obter dados em tempo real sobre condições climáticas, incluindo temperatura, umidade, vento e precipitação.
2. **Previsão do Tempo**: Oferece previsões meteorológicas para os próximos dias, permitindo que os usuários planejem atividades com base nas condições esperadas.

## Dependência: PyGithub

- **PyGithub**: Esta biblioteca fornece uma interface fácil de usar para interagir com a API do GitHub. Com o PyGithub, é possível realizar operações como:

  - **Autenticação**: Permite a autenticação usando tokens de acesso, facilitando a interação com repositórios privados e operações sensíveis.
  - **Gerenciamento de Repositórios**: Criação, edição, exclusão e consulta de repositórios no GitHub.
  - **Manipulação de Gists**: Permite publicar, editar e excluir gists, além de acessar informações sobre gists existentes.
  - **Gerenciamento de Issues e Pull Requests**: Criação, edição e consulta de issues e pull requests em repositórios, facilitando a colaboração em projetos.
  - **Acesso a Dados de Usuários**: Consulta a informações sobre usuários, organizações e repositórios públicos.

### Utilização no Projeto

A dependência `PyGithub` é fundamental para a funcionalidade de nossa API, permitindo que os usuários publiquem comentários em gists de forma programática. Por meio dessa biblioteca, nossa aplicação consegue interagir diretamente com a plataforma GitHub, oferecendo uma interface robusta e flexível para gerenciar comentários e gists.


## CI/CD
O projeto utiliza GitHub Actions para automatizar o processo de integração contínua (CI). O workflow é configurado para executar testes sempre que houver um push ou pull request para as branches main e develop. Isso garante que:

Os testes sejam executados em um ambiente Docker sempre que uma nova alteração for proposta.
Apenas pull requests com testes bem-sucedidos possam ser mesclados, ajudando a manter a integridade do código.
Como Funciona
Ao criar um pull request ou realizar um push para main ou develop, o GitHub Actions inicia a execução do workflow definido em .github/workflows/ci.yml.
O workflow constrói a imagem Docker e executa os testes automatizados.
O status da execução dos testes é exibido na interface do GitHub, permitindo que você veja rapidamente se os testes passaram ou falharam.