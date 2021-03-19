import requests

resp = requests.get('http://localhost:9999/echo/ben')
if resp.status_code == 200 and \
    resp.text == 'Say hello to my little friend: ben!':
    print('it worked! that almost never happens!')
else:
    print('Argh, got this:', resp.text)