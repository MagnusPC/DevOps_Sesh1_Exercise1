from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a test app!"

@app.route('/echo', methods=['GET'])
def echo():
    message = request.args.get('message', 'No message provided')
    return f"You said: {message}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)