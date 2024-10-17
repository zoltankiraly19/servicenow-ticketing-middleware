from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_servicenow_data', methods=['POST'])
def get_servicenow_data():
    data = request.json
    token = data.get('access_token')

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # Assignment groupok lekérdezése
    response = requests.get('https://dev227667.service-now.com/api/now/table/sys_user_group', headers=headers)
    
    if response.status_code == 200:
        groups = response.json().get('result', [])
        return jsonify({"assignment_groups": groups}), 200
    else:
        return jsonify({"error": "Failed to retrieve assignment groups", "details": response.text}), 400

if __name__ == '__main__':
    app.run(debug=True)
