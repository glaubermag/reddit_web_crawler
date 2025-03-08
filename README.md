# Reddit Data Scraper: Coleta, Armazenamento e Análise de Dados do Reddit

Este projeto consiste em um conjunto de scripts Python projetados para coletar, armazenar e analisar dados de posts e comentários do Reddit, utilizando um banco de dados PostgreSQL.

## Visão Geral

O projeto é composto pelos seguintes módulos principais:

* **Coleta de Dados (`functions/scrape_reddit_forum.py`):** (Este arquivo não está nos arquivos fornecidos, mas é citado no `main.py`) Responsável por acessar o Reddit e coletar informações sobre posts e comentários.
* **Manipulação do Banco de Dados (`connection/database_handler.py`):** Define as operações de criação de tabelas, inserção de dados e conexão com o PostgreSQL.
* **Funções de Consulta (`functions/get_all_posts.py`, `functions/get_top_reacted_comments.py`, `functions/get_comments_for_post.py`):** Fornecem consultas para recuperar dados do banco de dados, como todos os posts, comentários mais reagidos e comentários de um post específico.
* **Ponto de Entrada (`main.py`):** Orquestra a coleta e armazenamento de dados, chamando as funções dos outros módulos.
* **Schema do banco de dados (`schema.sql`)**: Define a estrutura das tabelas do banco de dados.

## Instalação e Configuração

1.  **Instalar o PostgreSQL:**
    * Certifique-se de que o PostgreSQL esteja instalado e em execução em sua máquina.

2.  **Criar um banco de dados:**
    * Crie um banco de dados PostgreSQL para armazenar os dados do Reddit. Você pode usar o `psql` ou uma ferramenta gráfica como o pgAdmin.

3.  **Clonar o repositório (se disponível):**
    ```bash
    git clone [URL_DO_REPOSITÓRIO] # Se o projeto estiver em um repositório Git.
    cd reddit_scrap
    ```

4.  **Instalar as dependências:**
    ```bash
    pip install requests beautifulsoup4 psycopg2-binary python-dotenv
    ```

5.  **Configurar o arquivo `.env`:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione as seguintes variáveis de ambiente, substituindo pelos seus valores:
    ```
    DB_NAME=postgres # ou o nome que você criou
    DB_USER=postgres # ou seu usuário
    DB_PASSWORD=teste # ou sua senha
    DB_HOST=localhost
    DB_PORT=5432
    ```

## Executando o Programa

1.  **Executar o `main.py` para Coletar e Armazenar Dados:**

    ```bash
    python main.py
    ```
    Este comando irá executar o `main.py`, que por sua vez irá:
    * Criar as tabelas no banco de dados (caso não existam).
    * Scrapear o subreddit configurado (isso depende de como o `scrape_reddit_forum` está configurado, que não foi fornecido).
    * Inserir os posts e seus comentários no banco de dados.
    * Mostrar a mensagem "Dados armazenados com sucesso!".

2.  **Consultar os posts**:

    * Executar `get_all_posts.py`:
    ```bash
    python functions/get_all_posts.py
    ```

## Análise do Código e Requisitos

**Dados Coletados:** O código coleta dados de posts e comentários do Reddit.

* **Posts:** URL, data da postagem, usuário, título, reações, conteúdo.
* **Comentários:** ID do post relacionado, autor, data, conteúdo, reações.

**Estrutura dos Dados:** Os dados são inerentemente relacionais. Um post pode ter vários comentários associados.

**Análise Futura:**

* **Análise de Sentimentos (NLP):** Isso envolve processar texto (conteúdo de posts e comentários) para entender o sentimento (positivo, negativo, neutro).
* **Previsão de Tendências:** Pode envolver análise temporal (quando os posts e comentários foram feitos) e correlação entre palavras-chave, tópicos e sentimentos.

**Persistência:** Os dados precisam ser armazenados de forma persistente, e a escolha da tecnologia de banco de dados é crucial.

**Consultas:** Deve haver pelo menos 3 formas diferentes de consultas.

## Escolha do Banco de Dados

Considerando a natureza relacional dos dados, a necessidade de consultas complexas e a maturidade da tecnologia, um **banco de dados relacional (SQL)** é a escolha mais adequada. Especificamente, o **PostgreSQL**, que já está sendo utilizado no código fornecido, é uma excelente opção pelas seguintes razões:

* **Relacional:** Ideal para modelar a relação entre posts e comentários.
* **Confiabilidade e Maturidade:** O PostgreSQL é um banco de dados robusto, confiável e com uma vasta comunidade.
* **SQL Padrão:** Suporte completo ao SQL padrão, permitindo consultas complexas e eficientes.
* **Tipos de Dados:** Suporta diversos tipos de dados, incluindo `TIMESTAMPTZ` (para datas e horários), `TEXT` (para conteúdo textual), `INTEGER` (para reações), etc.
* **Extensibilidade:** Possui recursos de extensibilidade que podem ser úteis no futuro, como índices de texto completo (para busca textual mais avançada) e extensões para análise geoespacial, se necessário.
* **Já está sendo utilizado:** O código já utiliza o Postgres, não sendo necessário alterar a estrutura existente.

## Modelagem dos Dados (já em `schema.sql`)

O arquivo `schema.sql` já define uma boa modelagem para os dados. Vamos analisar e confirmar as tabelas:

**posts:**

* `post_id` (SERIAL PRIMARY KEY): Identificador único do post.
* `data_coleta` (TIMESTAMPTZ NOT NULL): Data e hora em que o post foi coletado.
* `url_post` (TEXT UNIQUE NOT NULL): URL única do post no Reddit.
* `data_post` (TIMESTAMPTZ NOT NULL): Data e hora em que o post foi criado no Reddit.
* `usuario` (TEXT): Nome do usuário que fez o post.
* `titulo` (TEXT NOT NULL): Título do post.
* `reacoes_post` (INTEGER): Número de reações no post.
* `conteudo_post` (TEXT): Conteúdo do post.

**comments:**

* `comment_id` (SERIAL PRIMARY KEY): Identificador único do comentário.
* `post_id` (INTEGER REFERENCES posts(post_id) ON DELETE CASCADE): Chave estrangeira para o post ao qual o comentário pertence. `ON DELETE CASCADE` garante que se um post for deletado, seus comentários também serão.
* `autor` (TEXT): Autor do comentário.
* `data` (TIMESTAMPTZ): Data e hora em que o comentário foi feito.
* `conteudo` (TEXT): Conteúdo do comentário.
* `reacoes` (INTEGER): Número de reações no comentário.

## Implementação do Banco de Dados

O arquivo `schema.sql` já fornece a implementação da criação de tabelas.

O código em `database_handler.py` implementa as funções de conexão, criação de tabelas, inserção de dados e fechamento de conexão.