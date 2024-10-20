from flask import Flask, request, jsonify
import requests
from flask_cors import CORS  # CORS támogatás hozzáadása

app = Flask(__name__)
CORS(app)

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    data = request.json
    token = data.get('access_token')

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    ticket_data = {
        "short_description": data.get('short_description'),
        "assignment_group": data.get('assignment_group_sys_id'),  # Itt a sys_id-t küldjük el
        "priority": data.get('priority'),
        "caller_id": data.get('caller_id')
    }

    response = requests.post('https://dev227667.service-now.com/api/now/table/incident', json=ticket_data, headers=headers)

    if response.status_code == 201:
        return jsonify({"message": "Ticket created successfully", "ticket_number": response.json().get('result', {}).get('number')}), 201
    else:
        return jsonify({"error": "Failed to create ticket", "details": response.text}), 400

if __name__ == '__main__':
    app.run(debug=True)
