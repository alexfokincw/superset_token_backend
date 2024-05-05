from flask import Flask, jsonify
from flask_cors import CORS

import settings
from src.token_generator import get_token

app = Flask(__name__)
CORS(app, resources={r"/guest-token": {"origins": settings.FRONTEND_BASE_URL}})


@app.route('/guest-token', methods=['GET'])
def guest_token():
    token = get_token()
    return jsonify({"token": token})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
