#!/usr/bin/env python3

import string
import random
import json

from functools import wraps
from flask import Flask, jsonify, abort, render_template, request, Response
from werkzeug.exceptions import HTTPException

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

token = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(24))
data = {
    'developers': {
        'description': 'Project developers',
        'created_at': '2020-01-21T03:45:20',
        'members': ['billy', 'approvers', 'comitters', 'noelle'],
    },
    'admins': {
        'description': 'Administrators',
        'created_at': '2018-05-07T12:01:32',
        'members': ['alex', 'tristan', 'dj', 'julie']
    },
    'approvers': {
        'description': 'Code reviewers',
        'created_at': '2020-01-21T03:40:02',
        'members': ['admins']
    },
    'comitters': {
        'description': 'Project developers',
        'created_at': '2019-12-13T18:15:47',
        'members': ['andrew', 'ron', 'henry', 'janet']
    },
    'users': {
        'description': 'Other users',
        'created_at': '2019-10-31T14:50:55',
        'members': ['ashleigh', 'ron', 'james', 'henry']
    },
    'interest': {
        'description': 'People interested in project updates',
        'created_at': '2019-10-31T14:50:55',
        'members': ['ashleigh', 'alex', 'elliot', 'kori', 'maggie', 'users']
    },
}

def check_authorization(auth):
    parts = auth.split()
    return len(parts) == 2 and parts[0] == "Bearer" and parts[1] == token

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get('Authorization')
        if not auth or not check_authorization(auth):
            abort(401)
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
    group_data = data.get(group)
    if not group_data:
        abort(404, description=f"group '{group}' does not exist")

    return jsonify({
        'name': group,
        'description': group_data['description'],
        'created_at': group_data['created_at'],
    })

@app.route('/groups/<group>/members', methods=['GET'])
@requires_auth
def get_members(group):
    group_data = data.get(group)
    if not group_data:
        abort(404, description=f"group '{group}' does not exist")

    return jsonify([{"name": m} for m in group_data['members']])

@app.errorhandler(Exception)
def error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    return jsonify(error=str(e)), code

if __name__ == '__main__':
    print()
    print("  authentication token")
    print("  --------------------")
    print(" ", token)
    print()
    app.run(host="0.0.0.0")
