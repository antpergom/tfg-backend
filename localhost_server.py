from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/json_data', methods=["GET", "POST"])
def post_data():
    data = request.args.get("arg1")
    
    return format(data)



if __name__ == "__main__":
    app.run()