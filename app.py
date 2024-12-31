from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response(render_template('index.html'))
    # Añade las cabeceras necesarias
    response.headers['Cross-Origin-Opener-Policy'] = 'same-origin'
    response.headers['Cross-Origin-Embedder-Policy'] = 'require-corp'
    return response

if __name__ == '__main__':
    app.run(debug=True)
