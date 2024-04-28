from flask import Flask
from .routes import notification_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Enregistrement des blueprints sans préfixe pour simplifier l'accès
    app.register_blueprint(notification_bp, url_prefix='/')

    return app