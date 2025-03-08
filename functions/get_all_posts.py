import psycopg2
import os
import json

def get_all_posts_json():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password="teste",
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM posts;")
        posts = cur.fetchall()

        column_names = [desc[0] for desc in cur.description]

        posts_list = []
        for row in posts:
            posts_list.append(dict(zip(column_names, row)))

        return json.dumps(posts_list, indent=4, default=str) 

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    posts_json = get_all_posts_json()
    if posts_json:
        print(posts_json)