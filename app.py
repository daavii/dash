from flask import Flask
import requests
from lxml import html
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/scrape')
def scrape():
    # login session persists
    #session_requests = requests.session()

    #auth = $("[name=authenticity_token], body").val;



    # perf
    login_url = "https://auth.aiesec.org/users/sign_in"
    page = requests.get(login_url)
    
    print page

    root = html.parse(page)
    auth_token = root.xpath("//input[@name='authenticity_token']/@value")[0]
    print auth_token;

    '''
    tree = html.fromstring(result.text)
    console.log(tree);
    authenticity_token = list(set(tree.xpath("//input[@name='authenticity_token']/@value")))[0]
    


        # login information
    payload = {
        "user[email]": "gabriel.saruhashi@yale.edu", 
        "password": "Raptores1", 
        "commit": 'Sign in',
        "authenticity_token": $("[name=authenticity_token]", body).val()
    }

    result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
    )

    console.log(result);

    #url = 'https://bitbucket.org/dashboard/overview'
   # result = session_requests.get(
	#url, 
	#headers = dict(referer = url)
    )
        '''

