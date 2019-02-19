from flask import Flask
app = Flask(__name__)

global count
count = 0

@app.route('/', methods=['GET'])
def atomic():
    global count
    return str(count)

@app.route('/increment', methods=['POST'])
def increment():
    global count
    count = count + 1
    return '', 202
