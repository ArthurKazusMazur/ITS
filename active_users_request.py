from requests import get
from pprint import pprint

active_users = []

for page in range(1, 11):
    print(f'Страница {page} прочитана')
    json_data = get(f'https://gorest.co.in/public-api/users?page={page}').json()

    active_users.extend([user['name'] for user in json_data['data'] if user['status'] == 'Active'])

pprint(active_users)
