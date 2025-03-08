import requests
from bs4 import BeautifulSoup
import time
import os
from utils.generate_random_header import generate_random_headers
import datetime
from functions.scrape_reddit_post import scrape_reddit_post
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def scrape_reddit_forum():
    # Get the subreddit name from the .env file
    subreddit_name = os.getenv("SUBREDDIT_NAME")

    #Check if the subreddit_name exists
    if not subreddit_name:
        raise ValueError("SUBREDDIT_NAME not found in .env file.")

    # Construct the base URL using the subreddit name
    base_url = f'https://old.reddit.com/r/{subreddit_name}/'

    response = requests.get(base_url, headers=generate_random_headers(1)[0])

    if response.status_code != 200:
        return []  # Return an empty list in case of error

    soup = BeautifulSoup(response.text, 'html.parser')
    posts_data = []

    for post in soup.find_all('div', class_='thing'):
        if 'promoted' in post.get('class', []):
            continue  # Ignore sponsored posts

        # ------ Post Structure ------
        post_data = {
            'data_coleta': datetime.datetime.now().isoformat(),  # ISO for TIMESTAMPTZ
            'url_post': post.find('a', class_='title')['href'],
            'data_post': post.find('time')['datetime'] if post.find('time') else None,
            'usuario': post.find('a', class_='author').text if post.find('a', class_='author') else None,  # NULL if [deleted]
            'titulo': post.find('a', class_='title').text.strip(),
            'reacoes_post': int(post.find('div', class_='score').text.replace(' points', '')) if post.find('div', class_='score') else 0,  # Converting to INTEGER
            'conteudo_post': None,  # Will be filled in below
            'comentarios': []  # List of comments
        }

        # Correct URL if necessary
        if not post_data['url_post'].startswith('http'):
            post_data['url_post'] = f'https://old.reddit.com{post_data["url_post"]}'

        # ------ Collect Content and Comments ------
        post_content, comments = scrape_reddit_post(post_data['url_post'])
        post_data['conteudo_post'] = post_content
        post_data['comentarios'] = comments

        posts_data.append(post_data)
        time.sleep(2)

        # Limit for testing (optional)
        if len(posts_data) >= 5:
            break

    return posts_data  # Structured data for the database
