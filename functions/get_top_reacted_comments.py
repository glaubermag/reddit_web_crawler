import psycopg2
import os
import json

def get_top_reacted_comments_json(limit=5):
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password="teste",
            host='localhost',
            port='5432'
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM comments ORDER BY reacoes DESC LIMIT %s;", (limit,))
        comments = cur.fetchall()

        # Get column names
        column_names = [desc[0] for desc in cur.description]

        # Convert rows to dictionaries
        comments_list = []
        for row in comments:
            comments_list.append(dict(zip(column_names, row)))

        # Convert list of dictionaries to JSON
        return json.dumps(comments_list, indent=4, default=str)

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    top_comments_json = get_top_reacted_comments_json()
    if top_comments_json:
        print(top_comments_json)