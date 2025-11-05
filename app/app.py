from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from hardik !"

if __name__ == '__main__':
    # Important: host='0.0.0.0' lets it accept requests from outside Docker
    app.run(host='0.0.0.0', port=80)

