# from bottle import route, run

# @route('/')
# def home():
#     return "it isnt fancy, but its my home page"

# run(host='localhost', port=9999)
# 製作html檔案
# from bottle import route, run,static_file

# @route('/')
# def main():
#     return static_file('index.html', root='.')

# run(host='localhost', port=9999)
# 將引述傳至URL
from bottle import route, run,static_file

@route('/')
def home():
    return static_file('index.html', root='.')

@route('/echo/<thing>')
def echo(thing):
    return "Say hello to my little friend: %s!" % thing

run(host='localhost', port=9999)
# 
import requests

resp = requests.get('http://localhost:9999/echo/BEN')
if resp.status_code == 200 and \
    resp.text == 'Say hello to my little friend: ben!':
    print('it worked! that almost never happens!')
else:
    print('Argh, got this:', resp.text)




