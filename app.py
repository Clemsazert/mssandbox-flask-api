from flask import Flask, json
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/healthcheck')
def hello_world():
    return app.response_class(
        response=json.dumps({"status": "up",
                             "version": "0.0.1",
                             "environment": "development"}),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
