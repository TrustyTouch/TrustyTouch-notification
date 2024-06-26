from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)

    from .routes import notification_bp
    app.register_blueprint(notification_bp)

    return app

app = create_app()

cors = CORS(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
