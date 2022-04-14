"""
    A counter func.
    Copy the counter func into your program folder.
    """
import json
def setup_counter():
    n = 1
    with open("counter.json","w") as file:
        json.dump(n, file)
def counter():
    with open("counter.json") as file_boj:
        json.load(file_boj)
        n = file_boj.list()
        if (n == n):
            n = int(n.strip()) + 1
            json.dump(n, file)
            return n
setup_counter()
counter()
