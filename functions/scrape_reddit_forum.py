import requests
from bs4 import BeautifulSoup
import time
from utils.generate_random_header import generate_random_headers        
import datetime
from functions.scrape_reddit_post import scrape_reddit_post

def scrape_reddit_forum():
    base_url = 'https://old.reddit.com/r/python/'
    response = requests.get(base_url, headers=generate_random_headers(1)[0])
    
    if response.status_code != 200:
        return []  # Retorna lista vazia em caso de erro
    
    soup = BeautifulSoup(response.text, 'html.parser')
    posts_data = []
    
    for post in soup.find_all('div', class_='thing'):
        if 'promoted' in post.get('class', []):
            continue  # Ignora posts patrocinados

        # ------ Estruturação do Post ------
        post_data = {
            'data_coleta': datetime.datetime.now().isoformat(),  # ISO para TIMESTAMPTZ
            'url_post': post.find('a', class_='title')['href'],
            'data_post': post.find('time')['datetime'] if post.find('time') else None,
            'usuario': post.find('a', class_='author').text if post.find('a', class_='author') else None,  # NULL se [deleted]
            'titulo': post.find('a', class_='title').text.strip(),
            'reacoes_post': int(post.find('div', class_='score').text.replace(' points', '')) if post.find('div', class_='score') else 0,  # Convertendo para INTEGER
            'conteudo_post': None,  # Será preenchido abaixo
            'comentarios': []  # Lista de comentários
        }

        # Corrigir URL se necessário
        if not post_data['url_post'].startswith('http'):
            post_data['url_post'] = f'https://old.reddit.com{post_data["url_post"]}'

        # ------ Coletar Conteúdo e Comentários ------
        post_content, comments = scrape_reddit_post(post_data['url_post'])
        post_data['conteudo_post'] = post_content
        post_data['comentarios'] = comments

        posts_data.append(post_data)
        time.sleep(2)

        # Limitar para testes (opcional)
        if len(posts_data) >= 5:
            break

    return posts_data  # Dados estruturados para o banco de dados