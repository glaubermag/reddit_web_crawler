import os
import json
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from connection.database_handler import DatabaseHandler

def get_top_reacted_comments_json(limit=5):

    db = DatabaseHandler()
    conn = None
    try:
        conn = db.connect()
        if conn:
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
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            db.close_connection()

if __name__ == "__main__":
    top_comments_json = get_top_reacted_comments_json()
    if top_comments_json:
        print(top_comments_json)
