from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hola, gracias por la oportunidad, saludos!'

if __name__ == '__main__':
    app.run()
