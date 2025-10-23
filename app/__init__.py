from flask import Flask
from app.auth.routes import auth_bp
from app.dashboard.routes import dashboard_bp

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')

    return app
