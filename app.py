from flask import Flask
import requests
from lxml import html

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/scrape')
def scrape():
    session_requests = requests.session()

    # Get login csrf token
    result = session_requests.get("https://auth.aiesec.org/users/sign_in")
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
    print authenticity_token
    # Create payload
    payload = {
        "username": USERNAME, 
        "password": PASSWORD, 
        "csrfmiddlewaretoken": authenticity_token
    }'''
    return "Scraping"


