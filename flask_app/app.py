from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello_kubernetes():
    return jsonify({
        "message": "Hello from Flask API on Kubernetes!",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
