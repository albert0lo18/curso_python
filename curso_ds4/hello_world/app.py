from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <p>Ir a <a href="/about">about</a></p>
        </body>
    </html>
    '''

@app.route('/about')
def about():
    return '''
    <html>
        <head>
            <title>About this page</title>
        </head>
        <body>
            <h1>Everything about this website.</h1>
            <p>Back to <a href="/">Hello World</a></p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
