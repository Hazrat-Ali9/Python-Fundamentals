import requests
def fetch_api(url):
    response = requests.get(url)
    return response.json()

