from factory import create_app

app = create_app()

if __name__ == '__main__':
    args = {
        'host': '127.0.0.1', 'port': 8080,
        'debug': True, 'load_dotenv': True
    }
    app.run(**args)
