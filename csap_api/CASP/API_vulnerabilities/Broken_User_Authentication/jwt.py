from crypt import methods
from datetime import datetime, timedelta
import json
import jwt, hashlib, psycopg2, os
from flask import request, abort, jsonify
from CASP import app

JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 180


def getConnection():
    conn = psycopg2.connect(host='localhost',
                            database='casp',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn



@app.route('/login', methods=['GET', 'POST'])  
def login():
    email = request.args.get('email')
    password = hashlib.md5(request.args.get('password').encode('utf-8')).hexdigest()
    conn = getConnection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE email=%(email)s',{"email":email})
    user = cur.fetchall()
    cur.close()
    conn.close()
    if(user[0][2] == email and user[0][3] == password):
        payload = {
            'user_id': user[0][0],
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        jwt_token = jwt.encode(payload, JWT_SECRET, JWT_ALGORITHM)
        return jsonify({'token': jwt_token})
    else:
        return abort(403)