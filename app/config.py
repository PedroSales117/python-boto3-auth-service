from dotenv import load_dotenv
import os

load_dotenv()

COGNITO_USER_POOL_ID = os.getenv('COGNITO_USER_POOL_ID')
COGNITO_CLIENT_ID = os.getenv('COGNITO_CLIENT_ID')
REGION_NAME = os.getenv('REGION_NAME')
