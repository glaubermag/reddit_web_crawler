import os
import json
import sys

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from connection.database_handler import DatabaseHandler

def get_all_posts_json(fields=None, truncate_content=0):
    """
    Retrieves all posts from the database and returns them as a JSON string.

    Args:
        fields (list, optional): A list of field names to include in the output.
            If None, all fields are included. Defaults to None.
        truncate_content (int, optional): The number of characters to truncate the
            'conteudo_post' to. If 0, the content is removed. Defaults to 0.

    Returns:
        str: A JSON string containing the posts, or None if an error occurred.
             Returns an empty JSON array if there are no posts.
    """
    db = DatabaseHandler()
    conn = None
    try:
        conn = db.connect()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM posts;")
            posts = cur.fetchall()

            column_names = [desc[0] for desc in cur.description]
            posts_list = []
            for row in posts:
                post_dict = dict(zip(column_names, row))

                #Add the number of comments
                cur.execute("SELECT COUNT(*) FROM comments WHERE post_id = %s;", (post_dict["post_id"],))
                count_comments = cur.fetchone()
                post_dict["number_of_comments"]= count_comments[0]

                # Remove redundant content or truncate it
                if truncate_content == 0:
                    post_dict.pop('conteudo_post')
                elif truncate_content > 0:
                    post_dict['conteudo_post'] = post_dict['conteudo_post'][:truncate_content] + "..." if len(post_dict['conteudo_post']) > truncate_content else post_dict['conteudo_post']

                # Select specific fields if provided
                if fields:
                    post_dict = {field: post_dict[field] for field in fields if field in post_dict}

                posts_list.append(post_dict)

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
    fields_to_include = ["post_id", "url_post", "titulo", "reacoes_post","number_of_comments"]  # Example fields
    posts_json = get_all_posts_json(fields=fields_to_include, truncate_content=0)
    if posts_json:
        print(posts_json)
