from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/helloworld', methods = ['GET'])
def hello_world():
    return jsonify({"hello":"world"}), 200