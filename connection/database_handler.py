import psycopg2
import os
from psycopg2 import sql
from psycopg2.extras import execute_batch
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DatabaseHandler:
    def __init__(self):
        # Get database credentials from environment variables
        self.dbname = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.conn = None  # Initialize conn as None

        # Check if all required environment variables are set
        if not all([self.dbname, self.user, self.password, self.host, self.port]):
            raise ValueError("Missing required database environment variables (DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT).")

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
            return self.conn
        except Exception as e:
            print(f"Error connecting database: {e}")
            return None

    def create_tables(self):
        if not self.conn:
            self.connect()
        self.cur.execute(open("schema.sql", "r").read())
        self.conn.commit()

    def insert_post(self, post_data):
        if not self.conn:
            self.connect()
        query = sql.SQL("""
            INSERT INTO posts (data_coleta, url_post, data_post, usuario, titulo, reacoes_post, conteudo_post)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (url_post) DO NOTHING
            RETURNING post_id;
        """)
        data = (
            post_data['data_coleta'],
            post_data['url_post'],
            post_data['data_post'],
            post_data['usuario'],
            post_data['titulo'],
            int(post_data['reacoes_post']),
            post_data['conteudo_post']
        )
        self.cur.execute(query, data)
        result = self.cur.fetchone()
        self.conn.commit()
        return result[0] if result else None

    def insert_comments(self, post_id, comments):
        if not self.conn:
            self.connect()
        query = sql.SQL("""
            INSERT INTO comments (post_id, autor, data, conteudo, reacoes)
            VALUES (%s, %s, %s, %s, %s);
        """)
        data = [
            (post_id, c['autor'], c['data'], c['conteudo'], int(c['reacoes']))
            for c in comments
        ]
        execute_batch(self.cur, query, data)
        self.conn.commit()

    def close_connection(self):
        if self.conn:
            self.cur.close()
            self.conn.close()
            self.conn = None
