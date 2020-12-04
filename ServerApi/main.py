from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def test():
    return jsonify(
        status=200,
        message="get on /"
    )

if __name__ == "__main__":
    app.run()