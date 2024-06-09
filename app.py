from flask import Flask, request, send_file
from pymongo import MongoClient
from datetime import datetime
import os
import requests

app = Flask(__name__)

host = os.environ["DB_HOST"]
password = os.environ["DB_PASS"]

MONGO_URI = f"mongodb+srv://{host}:{password}@cluster0.gurdfx8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)

db = client[os.environ['DB_NAME']]
collection = db[os.environ['DB_COLLECTION']]

def get_geo_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        if response.status_code == 200:
            geo_data = response.json()
            return f"{geo_data['country']}, {geo_data['regionName']}, {geo_data['city']} ({geo_data['lat']}, {geo_data['lon']})"
        else:
            return False
    except:
        return False
    
@app.route('/')
def index():
    return send_file('static/looking.gif', mimetype='image/gif')

@app.route('/pixel')
def pixel():
    email_id = request.args.get('id', 'unknown')
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    referrer = request.referrer
    accept = request.headers.get('Accept')
    accept_language = request.headers.get('Accept-Language')
    cookies = request.cookies
    connection = request.headers.get('Connection')
    content_encoding = request.headers.get('Content-Encoding')
    content_type = request.headers.get('Content-Type')
    referrer_policy = request.headers.get('Referrer-Policy')
    geo_location = get_geo_location(ip_address)

    log = {
        "timestamp": datetime.utcnow(),
        "email_id": email_id,
        "ip_address": ip_address,
        "user_agent": user_agent,
        "referrer": referrer,
        "accept": accept,
        "accept_language": accept_language,
        "cookies": str(cookies),
        "connection": connection,
        "content_encoding": content_encoding,
        "content_type": content_type,
        "referrer_policy": referrer_policy,
        "geo_location": geo_location
    }

    collection.insert_one(log)

    return send_file('static/pixel.png', mimetype='image/png')

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    if not os.path.exists('static/pixel.png'):
        with open('static/pixel.png', 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x00\x00\x02\x00\x01\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82')

    app.run(debug=True)
