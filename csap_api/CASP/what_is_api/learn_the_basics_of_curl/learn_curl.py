from CASP import app
from flask import request,jsonify

@app.route('/learning/curl')
def hello_world():
    return 'Congrats! You have now learnt how to make a simple API call using curl'

@app.route('/learning/curl/post', methods=["POST"])
def postCall():
    input_json = request.get_json(force=True) 
    dictToReturn = {'Registration':input_json['text']}
    return jsonify(dictToReturn)