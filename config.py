from dotenv import load_dotenv
load_dotenv()
import os

NETLIFY_API_TOKEN = os.environ.get("netlify_api_token")