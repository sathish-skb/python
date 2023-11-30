from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/greeting', methods=['GET'])
def get_greeting():
    return jsonify({'message': 'Hello, welcome to the Flask API!'})

@app.route('/api/greeting', methods=['POST'])
def post_greeting():
    data = request.get_json()
    name = data.get('name', 'Guest')
    return jsonify({'message': f'Hello, {name}!'})

if __name__ == '__main__':
    app.run(debug=True)
