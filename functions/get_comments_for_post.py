import psycopg2
import os
import json
import sys

def get_comments_for_post_json(post_url):

    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password="teste",
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT post_id FROM posts WHERE url_post = %s;", (post_url,))
        post_id = cur.fetchone()
        if post_id:
            cur.execute("SELECT * FROM comments WHERE post_id = %s;", (post_id[0],))
            comments = cur.fetchall()

            column_names = [desc[0] for desc in cur.description]

            comments_list = []
            for row in comments:
                comments_list.append(dict(zip(column_names, row)))

            return json.dumps(comments_list, indent=4, default=str)

        return json.dumps([], indent=4) 

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python get_comments_for_post.py <url_do_post>")
    else:
        post_url = sys.argv[1]  
        comments_json = get_comments_for_post_json(post_url)
        if comments_json:
            print(comments_json)