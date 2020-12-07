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

@app.route('/api/product/add', methods=['GET', 'POST'])
def addProduct():
    response = request.args
    if ("Product_name" in response
        and "Store_id" in response):
        
        product = Product()
        product.createProduct(response['Store_id'], response['Product_name'], response)
        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))

@app.route('/api/product/categories', methods=['GET', 'POST'])
def addProductCategories():
    response = request.args

    if ("Product_id" in response and "Categories" in response):


        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))
