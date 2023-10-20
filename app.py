import os

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    message = 'Hello'
    service = os.environ.get("K.SERVICE", "Unknown Service")
    revision = os.environ.get("K.REVISION","Unknown revision")

    return render_template('hello.html', message=message, service=service, revision=revision)

if __name__ == '__main__':
    server_port = os.environ.get("PORT", "8080")
    app.run(debug=False, port=server_port, host='0.0.0.0')