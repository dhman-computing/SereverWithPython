# this code is to check the condition of the server

import requests


url = "https://serverwithpython.dhimancomputing.repl.co"

r_g = requests.get(url)
print(r_g.text)
print(r_g.content)
print(r_g.headers)
print(r_g.status_code)