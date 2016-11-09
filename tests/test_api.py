import requests


r = requests.get('http://127.0.0.1:7777/api', data={'name': 'Frank','age':24})

print r.content
