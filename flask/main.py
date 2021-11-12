from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/helloworld', methods = ['GET'])
def hello_world():
    return jsonify({"hello":"world"}), 200

if __name__ == "__main__":
    app.run(ssl_context='adhoc')