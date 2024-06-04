from flask import Flask, jsonify

# Creates a Flask application instance
app = Flask(__name__)

# Create Health API Endpoint. Endpoint will return a JSON response w/ app health
@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'OK'})

# main method to start app
if __name__ == '__main__':
    app.run(debug=True)
    