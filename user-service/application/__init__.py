from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Cấu hình database và các thông số khác
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://cloudacademy:cloudacademy@user-db:3306/user'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    
    # Import và đăng ký blueprint
    from .user_api import user_api_blueprint
    app.register_blueprint(user_api_blueprint)
    
    # Add prometheus wsgi middleware
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    return app

if __name__ == '__main__':
    app = create_app()
    # run_simple là optional, bạn có thể dùng app.run() nếu trong development
    run_simple('0.0.0.0', 5000, app)