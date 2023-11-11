from flask import Flask
from gpt4all import GPT4All

app = Flask(__name__)
model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)