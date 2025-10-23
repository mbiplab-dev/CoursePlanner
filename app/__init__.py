from flask import Flask
from app.auth.routes import auth_bp
from app.dashboard.routes import dashboard_bp
from app.planner.routes import planner_bp

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = 'your-secret-key-here'  # Change in production
    app.config['SESSION_TYPE'] = 'filesystem'
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(planner_bp, url_prefix='/planner')

    return app