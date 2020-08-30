import requests


url = 'https://gorest.co.in/public-api/users'

for i in range(1, 11):
    param = dict(page=i)
    response = requests.get(url, params=param)
    data = response.json()
    i += 1
    a = data['data']
    print(a[0])


