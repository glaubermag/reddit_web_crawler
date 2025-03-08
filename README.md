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
  - [Exemplo de Retorno JSON da função `get_top_reacted_comments.py`](#exemplo-de-retorno-json-da-função-get_top_reacted_commentspy)
  - [Exemplo de Retorno JSON da função `get_all_posts.py`](#exemplo-de-retorno-json-da-função-get_all_postspy)
  - [Exemplo de Retorno JSON da função `get_comments_for_post.py "URL_DO_POST"`](#exemplo-de-retorno-json-da-função-get_comments_for_postpy-url_do_post)

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

## Exemplo de Retorno JSON da função `get_top_reacted_comments.py`

Após executar `main.py` (para coletar os dados) e em seguida o comando:

```bash
python .\functions\get_top_reacted_comments.py
```
O retorno da função será:

```bash

[
    {
        "comment_id": 22,
        "post_id": 8,
        "autor": "Ahmad_Azhar",
        "data": "2025-03-08 02:27:33+00:00",
        "conteudo": "This was my first observation after clicking on examples that loading speed is much higher as compared to Reflex.\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 42,
        "post_id": 8,
        "autor": "Sn3llius",
        "data": "2025-03-07 19:30:19+00:00",
        "conteudo": "Thanks for your attention. Hi I'm chris and also core developer at Rio.\n\n\nThe main differences are:\n\n\n\n\nwith Rio you don't need HTML and CSS for styling.\n\n\nin Rio you create your components mostly in classes, in Dash you will use a functional approach.\n\n\nRio handles the client-server communication for you.\n\n\nCompared to Dash, Rio is a much newer framework and doesn't have a big community yet.\n\n\n\n\nThere are many more differences, but I would appreciate it, if you could test it out and provide us with your feedback!\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 11,
        "post_id": 7,
        "autor": "thalissonvs",
        "data": "2025-03-08 12:29:56+00:00",
        "conteudo": "Maybe I've add requests to test something, I'll review. Thank's man\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 5,
        "post_id": 7,
        "autor": "ThinhOppa",
        "data": "2025-03-08 10:20:43+00:00",
        "conteudo": "Tks so much for sharing. Since it works on top of CDP, is there any option to connect existed browser using ws devtool ?\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 46,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 08:23:05+00:00",
        "conteudo": "The biggest example is the rio website itself! Other than that, you can also check out the \nlive examples\n.\n\n\nAs for optimizations, there are a bunch of different ones that we're considering. Server-side rendering, transpiling event handlers to JS so they can be run on the client side, rewriting some rio internals in rust... It's hard to decide which direction we want to go, honestly\n\n",
        "reacoes": 1
    }
]
```
--- 
## Exemplo de Retorno JSON da função `get_all_posts.py`

Após executar o comando:

```bash
python .\functions\get_all_posts.py
```
O retorno da função será:
```bash
[
    {
        "post_id": 1,
        "url_post": "https://old.reddit.com/r/Python/comments/1j1dkk8/sunday_daily_thread_whats_everyone_working_on/",
        "titulo": "Sunday Daily Thread: What's everyone working on this week?",
        "reacoes_post": 0,
        "number_of_comments": 2
    },
    {
        "post_id": 2,
        "url_post": "https://old.reddit.com/r/Python/comments/1j645mw/saturday_daily_thread_resource_request_and/",
        "titulo": "Saturday Daily Thread: Resource Request and Sharing! Daily Thread",
        "reacoes_post": 0,
        "number_of_comments": 0
    },
    {
        "post_id": 3,
        "url_post": "https://old.reddit.com/r/Python/comments/1j6d2wo/python_is_big_in_europe/",
        "titulo": "Python is big in Europe",
        "reacoes_post": 130,
        "number_of_comments": 0
    },
    {
        "post_id": 7,
        "url_post": "https://old.reddit.com/r/Python/comments/1j689ag/i_built_a_python_library_for_realistic_web/",
        "titulo": "I built a python library for realistic web scraping and captcha bypass",
        "reacoes_post": 105,
        "number_of_comments": 14
    },
    {
        "post_id": 8,
        "url_post": "https://old.reddit.com/r/Python/comments/1j5ofdj/rio_hits_100k_downloads_2k_github_stars_open/",
        "titulo": "Rio Hits 100K Downloads & 2K GitHub Stars \u2013 Open Source Python Web Apps",
        "reacoes_post": 363,
        "number_of_comments": 57
    },
    {
        "post_id": 13,
        "url_post": "https://old.reddit.com/r/Python/comments/1j61i82/polars_cloud_the_distributed_cloud_architecture/",
        "titulo": "Polars Cloud; the distributed Cloud Architecture to run Polars anywhere",
        "reacoes_post": 84,
        "number_of_comments": 7
    }
]
```
---
## Exemplo de Retorno JSON da função `get_comments_for_post.py "URL_DO_POST"`

Após executar o comando:

```bash
python .\functions\get_comments_for_post.py https://old.reddit.com/r/Python/comments/1j5ofdj/rio_hits_100k_downloads_2k_github_stars_open/
```
O retorno da função será:

```bash
[
    {
        "comment_id": 17,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 14:17:32+00:00",
        "conteudo": "Glad we got this one out! One step closer to 1.0\n\n\nI'm one of the devs, so if you guys have any questions let us know!\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 18,
        "post_id": 8,
        "autor": "poopatroopa3",
        "data": "2025-03-07 14:34:15+00:00",
        "conteudo": "How does it compare with Reflex?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 19,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 14:49:27+00:00",
        "conteudo": "Reflex is probably the _most_ similar Python framework to Rio. However, while Reflex uses react internally, the Python API ends up quite different and doesn't get most of the benefits that made react so popular in the first place. With Rio we've basically reimplemented much of the core react functionality in pure Python, giving you the full benefit of it. This also leads to really quick iteration times, because we don't have to compile a JS app every time you make changes. Just a quick reload, and one second later you can see your app live!\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 20,
        "post_id": 8,
        "autor": "magnomagna",
        "data": "2025-03-07 23:22:40+00:00",
        "conteudo": "How much can someone who's new to web development understand the core React functionality by learning Rio?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 21,
        "post_id": 8,
        "autor": "Macho_Chad",
        "data": "2025-03-07 22:29:04+00:00",
        "conteudo": "Oh, that\u2019s fancy.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 22,
        "post_id": 8,
        "autor": "Ahmad_Azhar",
        "data": "2025-03-08 02:27:33+00:00",
        "conteudo": "This was my first observation after clicking on examples that loading speed is much higher as compared to Reflex.\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 23,
        "post_id": 8,
        "autor": "P4nd4no",
        "data": "2025-03-07 15:15:27+00:00",
        "conteudo": "Hey, Rio dev here! Rio was also written from the ground-up for modern Python. Everything has type hints, which allows your IDE to really understand which values are available and provide you with suggestions and documentation. If something lights up red in a Rio project, you can be 99% sure there really is an issue.\nOne of our main motivation to build a python web app framework from scratch was to avoid the overhead and inefficiencies common in wrapped frameworks. This helps us to provide a cleaner developer experience. Many projects like reflex rely on popular libraries like React internally, but the core benefits and elegance of these libraries is often diluted in the process.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 24,
        "post_id": 8,
        "autor": "ohcomeon111",
        "data": "2025-03-07 15:13:14+00:00",
        "conteudo": "Apart from React, how is it different from nicegui?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 25,
        "post_id": 8,
        "autor": "P4nd4no",
        "data": "2025-03-07 15:17:45+00:00",
        "conteudo": "Hi, rio dev here. I'm not very familiar with NiceGUI, but it seems like a more powerful version of Streamlit. Rio apps are built using reusable components inspired by React, Flutter, and Vue. These components are combined declaratively to create modular and maintainable UIs. In Rio you define components as simple dataclasses with a React/Flutter style build method. Rio continuously watches your attributes for changes and updates the UI as necessary. Rio has per-component state management, while NiceGUI appears to use session state. (But not 100% sure)\n\n\nWith Rio, you don't need to learn CSS, Tailwind, Vue, or Quasar.\n\n\nBoth NiceGUI and Rio are valid options for smaller web apps. However, Rio might offer easier and more maintainable code as your project grows. It provides reactive state management and allows you to build complex, arbitrarily nested UI layouts with concise syntax.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 26,
        "post_id": 8,
        "autor": "FUS3N",
        "data": "2025-03-07 18:14:06+00:00",
        "conteudo": "I have seen libraries that do this frontend and backend in python lag, like how even reflexes home page lags or even rios home page did lag a bit on the animation and feels a bit slugish like when i clicked example i had to wait a solid 30 seconds before anything happend, or navigation takes a bit to work, is it a limitation or is it just me?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 27,
        "post_id": 8,
        "autor": "DuckDatum",
        "data": "2025-03-08 02:38:17+00:00",
        "conteudo": "Any chance you can set up a PWA with it, service workers, etc? I\u2019ve been waiting for a python framework that will let me build webapps I can basically sideload onto my phone by opening in a browser and clicking \u201csave.\u201d\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 28,
        "post_id": 8,
        "autor": "thebouv",
        "data": "2025-03-07 15:00:39+00:00",
        "conteudo": "What\u2019s the output? Vanilla html/css/js?\n\n\nSee that it\u2019s not perfectly responsive. Modals in the CRUD example for instance overflow the viewport by a lot.\n\n\nHow easy would it be for me as a dev to fix that?\n\n\nHow easy it to adjust the themes?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 29,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 15:11:05+00:00",
        "conteudo": "The apps are written in Python and hosted as is. They are never converted to another language. Maybe have a look at the tutorial, it should clear things up.\n\n\nComponents are as large as they need to be to fit their content. If something is larger than the screen, that's either because the content requires it to be that large, or because a `min_width` / `min_height` was explicitly assigned. That's all up to your control.\n\n\nAs for themes, `rio.Theme` contains color palettes for different environments. For example, the top-level components of your app start out using the \"background\" palette, but the contents of a button use the secondary palette. You can freely change all colors.\n\n\nIf you want more radical style changes, you can create components yourself, by combining more basic ones, like Rectangles - just like you'd do in the browser. The cookbook has some examples of that, like a completely custom dropdown.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 30,
        "post_id": 8,
        "autor": "thebouv",
        "data": "2025-03-08 01:33:19+00:00",
        "conteudo": "At the end of the day, it must be outputting HTML/CSS at a minimum since, you know, it\u2019s displaying in a browser. You may write Python, but what\u2019s being viewed is the output which is HTML and CSS at a minimum. Same is if I write a Django or Flask or etc etc website. \n\n\nI point out the modal issue because, on mobile, the output is too large for the mobile screen. So, it\u2019s a bug in the example. It is too wide. So, not responsive to this iPhone. I\u2019m merely pointing it out the flaw in the example.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 31,
        "post_id": 8,
        "autor": "Sn3llius",
        "data": "2025-03-08 09:45:09+00:00",
        "conteudo": "good catch thanks, I'll fix it :)\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 32,
        "post_id": 8,
        "autor": "fat_abbott_",
        "data": "2025-03-07 14:34:02+00:00",
        "conteudo": "How is this better than streamlit?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 33,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 14:47:42+00:00",
        "conteudo": "Streamlit works well for small prototypes, but doesn't scale up to large production apps in my experience. If you are making a serious website for yourself or a department, Rio is the way to go\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 34,
        "post_id": 8,
        "autor": "ghostphreek",
        "data": "2025-03-07 17:03:06+00:00",
        "conteudo": "This is actually the exact issue that we had with streamlit as we started to scale up our internal app.\n\n\nWill check Rio out!\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 35,
        "post_id": 8,
        "autor": "Calimariae",
        "data": "2025-03-07 15:09:02+00:00",
        "conteudo": "Never heard of this before, but it looks interesting. Gonna give it a try. Thanks :)\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 36,
        "post_id": 8,
        "autor": "GlobeTrottingWeasels",
        "data": "2025-03-07 15:26:00+00:00",
        "conteudo": "I'll check it out - have you tried deploying it on AWS Lambda? For small scale sites I very much like doing that with Flask and API Gateway\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 37,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 15:37:11+00:00",
        "conteudo": "We have all of our deployments either in docker or kubernetes. If you call `as_fastapi` on your app you can get a FastAPI (and thus ASGI) app that you can deploy anywhere that supports ASGI.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 38,
        "post_id": 8,
        "autor": "luisote94",
        "data": "2025-03-07 15:44:18+00:00",
        "conteudo": "Is there support for plug-ins like drag n drop, offline apps, animation, scss?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 39,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 16:33:53+00:00",
        "conteudo": "Offline apps are supported out of the box - no extension needed. Also, Rio's whole jam is to be 100% Python, so since there is no CSS, you'll never need SCSS either :)\n\n\nDrag & drop is limited. We have a `rio.FilePickerArea` component that allows users to drop files to upload, but there isn't anything custom right now. Are you thinking of anything specific you'd like to see added?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 40,
        "post_id": 8,
        "autor": "luisote94",
        "data": "2025-03-07 17:13:39+00:00",
        "conteudo": "Oh nice thanks! I'm just thinking of different styling I would want in a web app. I usually use Bootstap for styling.\n\n\nI am looking for drag n drop like jquery ui where you can declare objects as draggable and can drag across the window, re-ordering ui elements, etc.\n\n\nNot sure about animations yet. I am trying to make an eReader type app where the pages flip like a book. \n\n\nThings like this\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 41,
        "post_id": 8,
        "autor": "schwanne",
        "data": "2025-03-07 17:52:13+00:00",
        "conteudo": "Cool to see! I've done a ton of web apps with Dash.  How does it compare?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 42,
        "post_id": 8,
        "autor": "Sn3llius",
        "data": "2025-03-07 19:30:19+00:00",
        "conteudo": "Thanks for your attention. Hi I'm chris and also core developer at Rio.\n\n\nThe main differences are:\n\n\n\n\nwith Rio you don't need HTML and CSS for styling.\n\n\nin Rio you create your components mostly in classes, in Dash you will use a functional approach.\n\n\nRio handles the client-server communication for you.\n\n\nCompared to Dash, Rio is a much newer framework and doesn't have a big community yet.\n\n\n\n\nThere are many more differences, but I would appreciate it, if you could test it out and provide us with your feedback!\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 43,
        "post_id": 8,
        "autor": "bacondota",
        "data": "2025-03-07 20:58:33+00:00",
        "conteudo": "Sounds interesting, will check it sometime.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 44,
        "post_id": 8,
        "autor": "w_w_flips",
        "data": "2025-03-07 23:22:39+00:00",
        "conteudo": "Looks very interesting - to the extent that I might actually give python GUIs a shot!\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 45,
        "post_id": 8,
        "autor": "tyrowo",
        "data": "2025-03-08 00:23:26+00:00",
        "conteudo": "So cool!\n\n\nDo you have any examples of existing web apps/web pages built with Rio that I can check out? really curious how the performance is.\n\n\nAs for what's missing - are y'all considering compiling to WASM eventually? Or is that kind of impossible? That was a pretty huge upgrade when I was working with Flutter Web apps.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 46,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 08:23:05+00:00",
        "conteudo": "The biggest example is the rio website itself! Other than that, you can also check out the \nlive examples\n.\n\n\nAs for optimizations, there are a bunch of different ones that we're considering. Server-side rendering, transpiling event handlers to JS so they can be run on the client side, rewriting some rio internals in rust... It's hard to decide which direction we want to go, honestly\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 47,
        "post_id": 8,
        "autor": "androidpam",
        "data": "2025-03-08 01:32:56+00:00",
        "conteudo": "I\u2019m upvoting this now and checking out GitHub later.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 48,
        "post_id": 8,
        "autor": "chrischmo",
        "data": "2025-03-08 09:01:53+00:00",
        "conteudo": "Looks very promising, good job! I haven't found any references to or examples for ORMs like SQLAlchemy. Is it currently possible to develop DB-backed apps with it, including rights management like user roles/groups (ideally with row-level security)?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 49,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 10:40:19+00:00",
        "conteudo": "This is of course possible, since Rio is just plain ol' python and allows you to use any database or ORM you want. But I think you're overestimating the \"scope\" of Rio. Rio is just a GUI framework; it doesn't handle stuff like user accounts or permissions. You should look for dedicated libraries for that purpose and use them together with Rio.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 50,
        "post_id": 8,
        "autor": "chrischmo",
        "data": "2025-03-08 11:21:14+00:00",
        "conteudo": "Thank you for the clarification!\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 51,
        "post_id": 8,
        "autor": "maxxfrag",
        "data": "2025-03-07 18:51:29+00:00",
        "conteudo": "Does it provide charting / diagramming conponents?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 52,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-07 18:59:08+00:00",
        "conteudo": "Yes, there's \nrio.Plot\n. It supports matplotlib, seaborn and plotly.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 53,
        "post_id": 8,
        "autor": "maxxfrag",
        "data": "2025-03-07 19:01:16+00:00",
        "conteudo": "Sounds great, i will definitely give it a try. Thx.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 54,
        "post_id": 8,
        "autor": "caprine_chris",
        "data": "2025-03-07 20:02:35+00:00",
        "conteudo": "This is fantastic! Sounds like Elixir LiveView in Python? Would be cool to see this expanded to work for mobile / native app development as well.\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 55,
        "post_id": 8,
        "autor": "Sones_d",
        "data": "2025-03-07 20:38:58+00:00",
        "conteudo": "It seems less complete than Reflex. Have you ever done a comparison? In what sense is rio better?\n\n",      
        "reacoes": 1
    },
    {
        "comment_id": 56,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-07 21:15:27+00:00",
        "conteudo": "It's true that Rio isn't as mature as Reflex, but it does have a number of advantages:\n\n\n\n\nIn Rio, state is stored in components, not a global \nrx.State\n class. Reflex's approach is fine for small apps, but can get messy in larger apps.\n\n\nRio really is pure python. You don't have to know anything about HTML or CSS at all.\n\n\nRio comes with an \"inspector\" tool. If your layout isn't working as expected, you can open this tool and it'll explain to you in english sentences why a component is layouted the way it is.\n\n\nRio has much faster hot reloading, which is nice during development. Reflex apps can take quite a while to reload because they go through a Javascript compiler.\n\n\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 57,
        "post_id": 8,
        "autor": "Sones_d",
        "data": "2025-03-07 21:22:00+00:00",
        "conteudo": "Awesome! Thanks for the answer.\nDo you guys have a way of wrapping custom react components?\nWould be possible to create a dicom viewer with rio?\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 58,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-07 21:54:11+00:00",
        "conteudo": "Sadly there's no interface for creating custom react or javascript components yet. We've been thinking about how to implement this for a while, but if we're not careful then these components might be incompatible with the optimizations we've got planned for the future.\n\n\nI should mention, you can always take a \nrio.Webview\n and throw arbitrary HTML and Javascript into it. It's not a nice way to implement a custom component though, haha\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 59,
        "post_id": 8,
        "autor": "wildcall551",
        "data": "2025-03-08 00:43:17+00:00",
        "conteudo": "Does Rio use Redux internally for state management or if it could be integrated with this library while building some app?\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 60,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 08:35:35+00:00",
        "conteudo": "Not really. With Rio you write everything in python, so a Javascript framework won't do you much good.\n\n", 
        "reacoes": 0
    },
    {
        "comment_id": 61,
        "post_id": 8,
        "autor": "ObeseTsunami",
        "data": "2025-03-08 00:44:10+00:00",
        "conteudo": "I\u2019ll play around with it! I like Django because of its straightforward framework of views, urls, models, and templates, but I HATE HTML and CSS. So I\u2019m excited to see what this can change for someone like me who loves the backend coding aspect but can\u2019t stand the tedium of CSS design.\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 62,
        "post_id": 8,
        "autor": "EnterTheJourney",
        "data": "2025-03-08 01:13:02+00:00",
        "conteudo": "Any plans on a searchbar with customisesble autocomplete? I did not find any compareable feature in other frameworks. Streamlit wasn\u2019t performant enough with local data and in other apps it was not easy to implement without getting into react first\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 63,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 08:30:33+00:00",
        "conteudo": "It's technically possible, but not super easy to do. You basically have to take a \nrio.TextInput\n and a \nrio.Popup\n and glue them together. The \ncustom dropdown example\n might give you a rough idea of how it would work\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 64,
        "post_id": 8,
        "autor": "bregmadaddy",
        "data": "2025-03-08 04:36:15+00:00",
        "conteudo": "Is there a lite version of Rio that can be compiled to Wasm (maybe via Pyodide)? Or is FastAPI preventing this from happening?\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 65,
        "post_id": 8,
        "autor": "Rawing7",
        "data": "2025-03-08 08:42:06+00:00",
        "conteudo": "This is quite an interesting idea, I'll have to look into this! Currently it won't work though because of the client-server communication. All of that code would have to be rewritten to work exclusively on the client side.\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 66,
        "post_id": 8,
        "autor": "theLastNenUser",
        "data": "2025-03-08 08:43:07+00:00",
        "conteudo": "Really cool project! I didn\u2019t find a \u201chow it works under the hood\u201d tutorial from clicking around for a couple minutes, but I\u2019m reading that things are running in python when this is being served. Are there any latency comparisons between some example apps built in Rio vs regular React? Would be good to know how much performance is traded off for convenience (if any)\n\n",
        "reacoes": 1
    },
    {
        "comment_id": 67,
        "post_id": 8,
        "autor": "ara-kananta",
        "data": "2025-03-07 15:07:29+00:00",
        "conteudo": "Do you have?\n\n\n\n\nRate Limiter\n\n\nOpenAPI\n\n\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 68,
        "post_id": 8,
        "autor": "mad-beef",
        "data": "2025-03-07 15:38:24+00:00",
        "conteudo": "Rio apps are ultimately FastAPI apps. Anything you can find for FastAPI exists for Rio as well. With that said, you don't have to write any HTTP routes with Rio, so there's really no need for OpenAPI :)\n\n\nRemember this is an App framework, not a HTTP framework. Think Flutter, Gtk, QT, React, etc\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 69,
        "post_id": 8,
        "autor": "ara-kananta",
        "data": "2025-03-07 15:41:26+00:00",
        "conteudo": "I see, i misunderstand it\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 70,
        "post_id": 8,
        "autor": "thedeepself",
        "data": "2025-03-07 21:50:47+00:00",
        "conteudo": "Did you look at other API Frameworks besides fast api? E.g. Sanic, Litestar, etc.\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 71,
        "post_id": 8,
        "autor": "the-scream-i-scrumpt",
        "data": "2025-03-07 18:46:25+00:00",
        "conteudo": "will this always be web-only? any plans for mobile?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 72,
        "post_id": 8,
        "autor": "OneWhiteNight",
        "data": "2025-03-07 22:05:45+00:00",
        "conteudo": "How does it compare to Shiny?\n\n",
        "reacoes": 0
    },
    {
        "comment_id": 73,
        "post_id": 8,
        "autor": "ioTeacher",
        "data": "2025-03-08 00:10:03+00:00",
        "conteudo": "About Database support ? (a LAMP fan, willing to move to Rio)\n\n",
        "reacoes": 0
    }
]
```