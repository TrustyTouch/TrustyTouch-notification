from flask import Flask
from .routes import notification_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Enregistrement des blueprints
    app.register_blueprint(notification_bp, url_prefix='/notifications')

    return app