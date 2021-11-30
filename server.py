import connexion
from flask import render_template

import config

app = config.connex_app
app.add_api('swagger.yml')


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True) # Para Windows
    # app.run(host='0.0.0.0', port=5000, debug=True) # Para Linux/Mac
