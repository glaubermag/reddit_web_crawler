import requests
from bs4 import BeautifulSoup
import time
from utils.generate_random_header import generate_random_headers

def scrape_reddit_post(url):
    response = requests.get(url, headers=generate_random_headers(1)[0])
    if response.status_code != 200:
        return None, []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extrair conteúdo do post
    post_content = soup.find('div', {'class': 'md'}).get_text(separator='\n') if soup.find('div', {'class': 'md'}) else ''
    
    # Extrair comentários
    comments = []
    for comment in soup.find_all('div', class_='comment'):
        # Extrair reações e remover 'point'/'points' e caracteres não numéricos
        raw_reacoes = comment.find('span', class_='score').text if comment.find('span', class_='score') else '0'
        reacoes_clean = raw_reacoes.replace(' point', '').replace(' points', '').strip()  # Remove textos
        reacoes = int(reacoes_clean) if reacoes_clean.isdigit() else 0  # Garante conversão

        comment_data = {
            'autor': comment.find('a', class_='author').text if comment.find('a', class_='author') else '[deleted]',
            'data': comment.find('time')['datetime'] if comment.find('time') else '',
            'conteudo': comment.find('div', class_='md').get_text(separator='\n') if comment.find('div', class_='md') else '',
            'reacoes': reacoes  # Agora é um inteiro!
        }
        comments.append(comment_data)
        time.sleep(0.5)

    return post_content, comments