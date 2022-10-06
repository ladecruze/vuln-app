import secrets, os, psycopg2, hashlib, bson
from flask import abort, render_template, request, Flask, jsonify
from flasgger import Swagger
from flask_mongoengine import MongoEngine
import pymongo

app = Flask(__name__)

import CASP.API_vulnerabilities.BOLA.Exploiting_IDOR_vulnerability.app
import CASP.API_vulnerabilities.Broken_User_Authentication.jwt
import CASP.what_is_api.learn_the_basics_of_curl.learn_curl

def getConnection():
    conn = psycopg2.connect(host='localhost',
                            database='casp',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

db = myclient["casp"]
dbcoll = db["collection"]
item_1 = {"id" : "U1IT00002","item_name" : "Egg","category" : "food","quantity" : 12,"price" : 36,"item_description" : "brown country eggs"}
item_2 = {"id" : "U1IT00003","item_name" : "Egg","category" : "food","quantity" : 12,"price" : 36,"item_description" : "brown country eggs"}
dbcoll.insert_many([item_1,item_2])

db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()

swagger = Swagger(app)

class User(db.Document):
    name = db.StringField()
    email = db.StringField()

@app.route('/mongo', methods=['GET'])  
def get_data():
    """Returns a list of todo item
    ---
    produces:
    - ""
    responses:
      200:
        description: "list of tasks"
      400:
        description: "Invalid ID supplied"
      404:
        description: "todo item not found"
    """
    for i in dbcoll.find():
        print(i)
    items = dbcoll.find_one({"id":"Egg"})
    return items

#registration with mass assignment vulnerability
@app.route('/v1/register', methods=['GET', 'POST'])
def signup_user():
    """Register a new user
    ---
    produces:
    - "text/html"
    responses:
      200:
        description: "User has been"

      400:
        description: "Invalid ID supplied"
      404:
        description: "todo item not found"
    """  
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = hashlib.md5(request.args.get('password')).hexdigest()
        role = request.args.get('role')
        secret = secrets.token_urlsafe(32)
        conn = getConnection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users;')
        if(role is not None):
            cur.execute('INSERT INTO users (name, email, role, password, key) VALUES (%s, %s, %s, %s, %s)',(username, email, role, password, secret))
        else:
            cur.execute('INSERT INTO users (name, email, role, password, key) VALUES (%s, %s, %s, %s, %s)',(username, email, 'user',password, secret))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(message='registered successfully',apikey=secret)
    if request.method == 'GET':
        return render_template('register.html')

@app.route('/v1/getkey', methods=['GET', 'POST'])  
def get_api_key():
    """Log in to get API key
    ---
    produces:
    - "application/json"
    responses:
      200:
        description: ""
      400:
        description: "Invalid ID supplied"
      404:
        description: "todo item not found"
    """
    if request.method == 'POST':
        email = request.form.get('email')
        password = hashlib.md5(request.form.get('password').encode('utf8')).hexdigest()
        print(password)
        conn = getConnection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE email=%(email)s',{"email":email})
        users = cur.fetchall()
        print(users)
        cur.close()
        conn.close()
        try:
            if(users[0][2] == email and users[0][3] == password):
                return render_template('documentation.html',apikey=users[0][5])
            else:
                return abort(403)
        except IndexError:
            return "user not available"
    if request.method == 'GET':
        return render_template('login.html')