from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # CORS támogatás engedélyezése

app = Flask(__name__)
CORS(app)  # CORS támogatás biztosítása az alkalmazáshoz

@app.route('/get_token', methods=['POST'])
def get_token():
    # JSON formátumban érkező kérés
    data = request.json  
    
    # ServiceNow hitelesítési adatok
    auth_data = {
        'grant_type': 'password',
        'client_id': '45f3f2fb2ead4928ab994c64c664dfdc',
        'client_secret': 'fyHL1.@d&7',
        'username': data.get('username'),
        'password': data.get('password')
    }
    
    # Hitelesítés a ServiceNow felé
    response = requests.post('https://dev227667.service-now.com/oauth_token.do', data=auth_data)
    
    if response.status_code == 200:
        access_token = response.json().get('access_token')
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Authentication failed", "details": response.text}), 400

if __name__ == '__main__':
    app.run(debug=True)
