from functions.scrape_reddit_forum import scrape_reddit_forum
from connection.database_handler import DatabaseHandler


if __name__ == '__main__':
    dados = scrape_reddit_forum()
    db = DatabaseHandler()
    db.create_tables()
    for post in dados:
        post_id = db.insert_post(post)
        if post_id:
            db.insert_comments(post_id, post['comentarios'])
    db.close()
    print("Dados armazenados com sucesso!")