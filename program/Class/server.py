from flask import Flask, json, render_template, jsonify, request
import json
import sys
from Class.users import User
from Class.products import Product
from Class.stores import Store
from IA.EasyStock import IA

app = Flask(__name__)

@app.route('/api/stores/add', methods=['POST', 'GET'])
def addStores():
    response = request.args
    if ("Store_name" in response):
        store = Store()
        store.createStore(response['Store_name'], response)
        return(jsonify({'status':'ok'}))
    else:
        return(jsonify({'status':'ko'}))

@app.route('/api/product/add', methods=['POST', 'GET'])
def addProduct():
    response = request.args
    print("resp : ", response, file=sys.stderr)

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
            'response': response,
            'products': returnOfProduct
        }))
    except:
        return jsonify({
            'status':'ko'
        })

@app.route('/api/user/add', methods=['POST', 'GET'])
def addUser():
    response = request.args
    if ("User_name" in response and 
        "Password" in response and
        "Store" in response):
        user = User()
        if (user.createUser(response['User_name'], response['Password'], response['Store'], response) != -84):
            store = user.login(response["User_name"], response["Password"])
            return (jsonify({
                'status':'ok',
                'store_name':store['Store'],
                'Store_id': store["Store"]
            }))
        else:
            return (jsonify({
                'status':'ko'
            }))
    else:
        return (jsonify({
            'status':'ko'
        }))

@app.route('/api/user/login', methods=['POST', 'GET'])
def Login():
    response = request.args
    if ("User_name" in response and 
        "Password" in response):
        user = User()
        store = user.login(response["User_name"], response["Password"])

        return (jsonify({
            'status':'ok',
            'Store': store["Store_name"],
            'Store_id': store["Store"]
        }))
    else:
        return (jsonify({
            'status':'ko'
        }))