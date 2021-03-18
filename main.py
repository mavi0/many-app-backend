import requests
import json
import logging, coloredlogs
from flask import Flask, redirect, url_for, request, render_template, send_file, jsonify, make_response, abort

logger = logging.getLogger(__name__)
coloredlogs.install(level='INFO')

app = Flask(__name__)

def auth(request_id):
    with open('data/id.json') as f:
        users = json.load(f)
    for user in users.get("users"):
        if request_id == user.get("id"):
            logger.info("ID: " + request_id +  " authenticated as user " + user.get("username"))
            return True
    logger.info("ID: " + request_id +  " failed to authenticate")
    return False

@app.route('/api/pushresult', methods=['GET', 'POST'])
def push_result():
    result = json.loads(request.get_data().decode())
    if not auth(result.get("id")):
        result["id"] = 0
    
    logger.info("Result dump: " + result)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

@app.route('/api/authid', methods=['GET', 'POST'])
def auth_id():
    request_id = json.loads(request.get_data().decode()).get("id")
    if not auth(request_id):
        abort(404, description="ID not found")
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')