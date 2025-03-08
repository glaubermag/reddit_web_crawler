import psycopg2
from psycopg2 import sql
from psycopg2.extras import execute_batch

class DatabaseHandler:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password="teste",  # Replace with your password
            host='localhost',
            port='5432'
        )
        self.cur = self.conn.cursor()
    
    def create_tables(self):
        self.cur.execute(open("schema.sql", "r").read())
        self.conn.commit()
    
    def insert_post(self, post_data):
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
    
    def close(self):
        self.cur.close()
        self.conn.close()