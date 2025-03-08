# 📊 Reddit Data Scraper & Analyzer

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15%2B-brightgreen)](https://postgresql.org)
[![License](https://img.shields.io/badge/License-MIT-red)](LICENSE)

Este projeto permite a coleta e análise de posts e comentários do Reddit, armazenando os dados de maneira segura em um banco relacional PostgreSQL. Ele é ideal para pesquisadores, analistas de dados e desenvolvedores que desejam extrair informações valiosas de comunidades online. Com consultas pré-definidas, é possível obter insights rapidamente, facilitando a análise de tendências, identificação de padrões e integração com ferramentas de NLP para processamento avançado de linguagem natural.

---

## Índice

- [📊 Reddit Data Scraper \& Analyzer](#-reddit-data-scraper--analyzer)
  - [Índice](#índice)
  - [📌 Visão Geral](#-visão-geral)
  - [⚡ Quick Start](#-quick-start)
    - [1️⃣ Clonar o repositório](#1️⃣-clonar-o-repositório)
    - [2️⃣ Criar um ambiente virtual (opcional, mas recomendado)](#2️⃣-criar-um-ambiente-virtual-opcional-mas-recomendado)
    - [3️⃣ Instalar as dependências](#3️⃣-instalar-as-dependências)
    - [4️⃣ Configurar o arquivo `.env`](#4️⃣-configurar-o-arquivo-env)
    - [5️⃣ Executar o script principal](#5️⃣-executar-o-script-principal)
  - [🗄️ Modelagem do Banco de Dados](#️-modelagem-do-banco-de-dados)
    - [✔️ Por Que PostgreSQL?](#️-por-que-postgresql)
      - [📌 Instalação do PostgreSQL](#-instalação-do-postgresql)
  - [🔍 Funções de Consulta](#-funções-de-consulta)
  - [🧭 Roadmap](#-roadmap)
  - [👥 Contribuição](#-contribuição)
  - [🚨 Problemas Comuns](#-problemas-comuns)
    - [Erro "invalid literal for int()"](#erro-invalid-literal-for-int)

---

## 📌 Visão Geral

Um coletor de dados do Reddit que:

- Extrai posts e comentários de subreddits (configurável via variável de ambiente `SUBREDDIT_NAME`)
- Armazena os dados de forma segura em um banco PostgreSQL
- Oferece consultas pré-definidas para análise de dados (retornando JSON)
- Está pronto para integração com NLP
- Possui tratamento de erros durante a coleta de dados

---

## ⚡ Quick Start

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/glaubermag/reddit-scraper
cd reddit-scraper
```

### 2️⃣ Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate      # No Windows
```

### 3️⃣ Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 4️⃣ Configurar o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

```ini
DB_NAME=reddit_data
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
SUBREDDIT_NAME=Python # Nome do subreddit a ser coletado
```

### 5️⃣ Executar o script principal

```bash
python main.py
```

Saída esperada:

```bash
Coleta concluída. 5 posts armazenados.
```

Se ocorrer um erro, algumas mensagens comuns incluem:

```bash
psycopg2.OperationalError: could not connect to server: Connection refused
```
💡 **Solução:** Verifique se o PostgreSQL está em execução e se as credenciais no `.env` estão corretas.

```bash
KeyError: 'SUBREDDIT_NAME'
```
💡 **Solução:** Certifique-se de que o arquivo `.env` está corretamente configurado e contém todas as variáveis necessárias.

```bash
python main.py
```

Saída esperada:

```bash
Coleta concluída. 5 posts armazenados.
```

---

## 🗄️ Modelagem do Banco de Dados

O banco de dados PostgreSQL segue a estrutura:

```sql
posts
├─ post_id (PK)
├─ url_post (UNIQUE)
├─ titulo
└─ ...

comments
├─ comment_id (PK)
└─ post_id (FK → posts)
```

### ✔️ Por Que PostgreSQL?

- Suporte a JSONB para análise de texto
- Índices FULLTEXT para buscas eficientes
- Transações ACID para integridade dos dados

#### 📌 Instalação do PostgreSQL

- [Guia de Instalação Oficial](https://www.postgresql.org/download/)
- Criação do banco:

```sql
CREATE DATABASE reddit_data;
```

---

## 🔍 Funções de Consulta

| Arquivo                       | Descrição                         | Exemplo de Uso                                  |
| ----------------------------- | --------------------------------- | ----------------------------------------------- |
| `get_all_posts.py`            | Lista todos os posts              | `python get_all_posts.py`                       |
| `get_comments_for_post.py`    | Comentários de um post específico | `python get_comments_for_post.py "https://..."` |
| `get_top_reacted_comments.py` | Top 10 comentários mais curtidos  | `python get_top_reacted_comments.py`            |

---

## 🧭 Roadmap

- [ ] Implementar análise de sentimentos usando NLP
- [ ] Criar um painel de visualização de dados
- [ ] Suporte para múltiplos subreddits
- [ ] Melhorar o tratamento de erros e logging
- [ ] Implementar um sistema de alerta para novas tendências

---

## 👥 Contribuição

1. Faça um fork do projeto
2. Crie uma branch: `git checkout -b minha-feature`
3. Commit: `git commit -m 'Adicionei algo incrível'`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

---

## 🚨 Problemas Comuns

### Erro "invalid literal for int()"

```bash
# Causa: Texto nas reações (ex: "1 point")
# Solução: Atualize o código com:
git pull origin main
```

---





