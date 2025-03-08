import os
import json
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from connection.database_handler import DatabaseHandler

def get_all_posts_json():
    """
    Retrieves all posts from the database and returns them as a JSON string.

    Returns:
        str: A JSON string containing the posts, or None if an error occurred.
             Returns an empty JSON array if there are no posts.
    """
    db = DatabaseHandler()
    conn= None
    try:
        conn = db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM posts;")
            posts = cur.fetchall()

            column_names = [desc[0] for desc in cur.description]

            posts_list = []
            for row in posts:
                posts_list.append(dict(zip(column_names, row)))

            return json.dumps(posts_list, indent=4, default=str)
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            db.close_connection()

if __name__ == "__main__":
    posts_json = get_all_posts_json()
    if posts_json:
        print(posts_json)
