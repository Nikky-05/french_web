from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize db globally (but not bind to app yet)
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Initialize database with the app
    db.init_app(app)

    # Import blueprints and register them
    from app import routes
    app.register_blueprint(routes.bp)

    return app
