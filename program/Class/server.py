from flask import Flask, json, render_template, jsonify, request
import json
import sys
from Class.users import User
from Class.products import Product
from Class.stores import Store

app = Flask(__name__)

@app.route('/api/stores/add', methods=['GET', 'POST'])
def addStores():
    response = request.args
    if ("Store_name" in response):
        store = Store()
        store.createStore(response['Store_name'], response)
        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))
