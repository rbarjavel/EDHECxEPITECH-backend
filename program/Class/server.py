from flask import Flask, json, render_template, jsonify, request
import json
import sys
from Class.users import User
from Class.products import Product
from Class.stores import Store
from IA.EasyStock import IA

app = Flask(__name__)

@app.route('/api/stores/add', methods=['POST'])
def addStores():
    response = request.args
    if ("Store_name" in response):
        store = Store()
        store.createStore(response['Store_name'], response)
        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))

@app.route('/api/product/add', methods=['POST'])
def addProduct():
    response = request.args
    if ("Product_name" in response
        and "Store_id" in response):
        
        product = Product()
        product.createProduct(response['Store_id'], response['Product_name'], response)
        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))

@app.route('/api/product/getWithTags', methods=['GET'])
def getWithTags():
    response = request.args

    try:
        intelligence = IA()
        prod = Product()

        returnOfIa = intelligence.runProcesse(response['msg'])
        returnOfProduct = prod.sortProduct(returnOfIa)

        return(jsonify({
            'status':'ok',
            'IA': returnOfIa,
            'products': returnOfProduct
        }))
    except:
        return jsonify({
            'status':'ko'
        })

@app.route('/api/user/add', methods=['POST'])
def addUser():
    response = request.args
    if ("User_name" in response and 
        "Password" in response and
        "Store" in response):
        user = User()
        user.createUser(response['User_name'], response['Password'], response['Store'], response)

        return (jsonify({
            'status':'ok'
        }))
    else:
        return (jsonify({
            'status':'ko'
        }))