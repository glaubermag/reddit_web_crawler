import random

def generate_random_headers(num_headers=1):
  """
  Generates a list of random headers.

  Args:
    num_headers: The number of headers to generate.

  Returns:
    A list of dictionaries, where each dictionary represents a header.
  """

  headers = []
  for _ in range(num_headers):
    user_agent = f"Mozilla/5.0 ({random.choice(['Windows NT 10.0', 'Macintosh', 'X11; Linux x86_64'])}" \
                 f"; {random.choice(['Win64', 'Intel Mac OS X', 'x86_64'])}" \
                 f"; {random.choice(['x64', 'Intel Mac OS X 10_15_7', 'Linux'])}" \
                 f" AppleWebKit/{random.randint(537, 540)}.36 (KHTML, like Gecko)" \
                 f" Chrome/{random.randint(90, 100)}.0.{random.randint(4000, 5000)}.{random.randint(100, 200)} Safari/537.36"
    headers.append({'User-Agent': user_agent})

  return headers
