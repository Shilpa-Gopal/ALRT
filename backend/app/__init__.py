import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    
    # Use PostgreSQL database URL only
    database_url = os.getenv('DATABASE_URL')
    if not database_url:
        raise ValueError("DATABASE_URL environment variable must be set for PostgreSQL connection")
    
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'your-secret-key'  # Change in production
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

    CORS(app,
         resources={
             r"/api/*": {
                 "origins":
                 "*",
                 "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                 "allow_headers":
                 ["Content-Type", "X-User-Id", "Accept", "Authorization"],
                 "expose_headers": ["Content-Type"],
                 "supports_credentials":
                 True,
                 "max_age":
                 3600
             }
         })
    db.init_app(app)

    return app
