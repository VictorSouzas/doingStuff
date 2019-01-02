from flask import abort, Flask
app = Flask(__name__)


@app.route('/')
def hellp_world():
    return 'Hello, world!'


@app.route('/not_found', methods=['GET', ])
def not_found():
    abort(401)

if __name__ == '__main__':
    args = {
        'host': '127.0.0.1', 'port': 8080,
        'debug': True, 'load_dotenv': True
    }
    app.run(**args)
