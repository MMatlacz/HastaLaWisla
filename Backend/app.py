import json
from wsgiref import simple_server

from flask import Flask

app_url = ''
app = Flask(__name__)
app.debug = True


@app.route(app_url + '/places/')
def get_places():
    obj = {}
    obj['miejsce'] = 'Warszawa'
    obj['nazwa'] = 'bar'
    return json.dumps(obj)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 5000, app)
    httpd.serve_forever()
