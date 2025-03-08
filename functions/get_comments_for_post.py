import os
import json
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from connection.database_handler import DatabaseHandler  # Import DatabaseHandler

def get_comments_for_post_json(post_url):

    db = DatabaseHandler()  # Create an instance of DatabaseHandler
    conn = None  # Initialize conn outside the try block
    try:
        conn = db.connect() # Use connect() method from DatabaseHandler
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

        return json.dumps([], indent=4)  # Return empty list if post_id not found

    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        if conn:
            db.close_connection() # use close_connection() from DatabaseHandler

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python get_comments_for_post.py <url_do_post>")
    else:
        post_url = sys.argv[1]
        comments_json = get_comments_for_post_json(post_url)
        if comments_json:
            print(comments_json)
