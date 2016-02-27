from flask import Flask

app_url = ''
app = Flask(__name__)
app.debug = True

#cokolwiek Mikołaj

@app.route(app_url + '/places/')
def get_places():
    pass
