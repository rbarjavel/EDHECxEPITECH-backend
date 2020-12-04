from flask import Flask, jsonify

app = Flask(__name__)

def GetIndex():
    response = make_response(
        jsonify(
            {"message": str(FLAMSG_ERR_SEC_ACCESS_DENIED),
             "severity": "danger"}
        ),
        401,
    )
    response.headers
