from functions.scrape_reddit_forum import scrape_reddit_forum
from connection.database_handler import DatabaseHandler
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__ == '__main__':
    # Check if required variables exists
    if not all([os.getenv("DB_NAME"), os.getenv("DB_USER"), os.getenv("DB_PASSWORD"), os.getenv("DB_HOST"), os.getenv("DB_PORT"), os.getenv("SUBREDDIT_NAME")]):
        raise ValueError("Missing required database environment variables (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, SUBREDDIT_NAME).")
    
    #try to execute the scrape
    try:
      dados = scrape_reddit_forum()
    except Exception as e:
      print(f"Error scraping: {e}")
      exit()
    #try to execute the database operations
    try:
        db = DatabaseHandler()
        db.create_tables()
        for post in dados:
            post_id = db.insert_post(post)
            if post_id:
                db.insert_comments(post_id, post['comentarios'])
        db.close_connection()
        print("Dados armazenados com sucesso!")
    except Exception as e:
      print(f"Error manipulating database: {e}")
      db.close_connection()
      exit()
