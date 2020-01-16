#!/usr/bin/env python3

import string
import random
import json

from functools import wraps
from flask import Flask, jsonify, abort, render_template, request, Response

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(24))
data = {
    'developers': ['billy', 'approvers', 'comitters'],
    'admins': ['alex', 'tristan'],
    'approvers': ['admins'],
    'comitters': ['andrew', 'ron', 'henry'],
    'users': ['ron', 'henry', 'james'],
}

def check_authorization(auth):
    parts = auth.split()
    return len(parts) == 2 and parts[0] == "Bearer" and parts[1] == token

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or not check_authorization(auth):
            res = jsonify({'error': 'authentication required'})
            res.status_code = 401
            return res
        return f(*args, **kwargs)
    return decorated

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        token=token,
        data=data,
    )

@app.route('/groups', methods=['GET'])
@requires_auth
def get_groups():
    return jsonify([{"name": g} for g in data.keys()])

@app.route('/groups/<group>', methods=['GET'])
@requires_auth
def get_group(group):
    if group in data:
        return jsonify({"name": group})
    else:
        res = jsonify({'error': f"group '{group}' does not exist"})
        res.status_code = 404
        return res

@app.route('/groups/<group>/members', methods=['GET'])
@requires_auth
def get_members(group):
    members = data.get(group)
    if members:
        return jsonify([{"name": m} for m in members])
    else:
        res = jsonify({'error': f"group '{group}' does not exist"})
        res.status_code = 404
        return res


if __name__ == '__main__':
    print()
    print("  authentication token")
    print("  --------------------")
    print(" ", token)
    print()
    app.run(host="0.0.0.0")
