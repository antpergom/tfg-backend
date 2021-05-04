from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

"""
@app.route('/json_data', methods=["GET", "POST"])
def post_request_in():
    data = request.args.get("arg1")
    
    return format(data)
"""

@app.route('/', methods=["GET", "POST"])
def post_request_in():
    #data = request.args.get("arg1")
    data = request.json(force=True)
    
    return jsonify(data)


if __name__ == "__main__":
    app.run()