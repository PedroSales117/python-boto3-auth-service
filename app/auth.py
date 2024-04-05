from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError
from .config import COGNITO_USER_POOL_ID, COGNITO_CLIENT_ID, REGION_NAME

app = Flask(__name__)

cognito_client = boto3.client('cognito-idp', region_name=REGION_NAME)

def initiate_auth(username, password):
    try:
        resp = cognito_client.initiate_auth(
            ClientId=COGNITO_CLIENT_ID,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            }
        )
        return resp
    except ClientError as e:
        return None, str(e)

def register_user(username, password):
    try:
        cognito_client.sign_up(
            ClientId=COGNITO_CLIENT_ID,
            Username=username,
            Password=password,
        )
        return True, "User registered successfully"
    except ClientError as e:
        return False, e.response['Error']['Message']

@app.route('/signup', methods=['POST'])
def signup():
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    success, message = register_user(username, password)
    if success:
        return jsonify(message=message), 200
    else:
        return jsonify(error=message), 400

@app.route('/signin', methods=['POST'])
def signin():
    body = request.get_json()
    username = body.get('username')
    password = body.get('password')
    auth_response, error = initiate_auth(username, password)
    if auth_response:
        return jsonify(auth_response), 200
    else:
        return jsonify(error=error), 400

@app.route('/validate', methods=['POST'])
def validate_token():
    access_token = request.headers.get('Authorization')
    try:
        response = cognito_client.get_user(
            AccessToken=access_token
        )
        return jsonify(user=response['Username']), 200
    except ClientError as e:
        return jsonify(error=str(e)), 400
