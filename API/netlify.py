import requests
from config import NETLIFY_API_TOKEN

BASE_URL = "https://api.netlify.com/api/v1"

def get_headers():
    return {"Authorization": f"Bearer {NETLIFY_API_TOKEN}"}

def list_sites():
    url = f"{BASE_URL}/sites"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to list sites. Status code: {response.status_code}")
        return None
    
def list_forms(site_id):
    url = f"{BASE_URL}/sites/{site_id}/forms"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to list sites. Status code: {response.status_code}")
        return None

def list_form_submissions(form_id):
    url = f"{BASE_URL}/forms/{form_id}/submissions"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to list sites. Status code: {response.status_code}")
        return None

"""
GET /sites/{site_id}/builds
"""
def list_builds(site_id):
    url = f"{BASE_URL}/sites/{site_id}/builds"
    headers = get_headers()
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to list sites. Status code: {response.status_code}")
        return None