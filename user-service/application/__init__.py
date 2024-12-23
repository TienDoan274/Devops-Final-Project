import config
import os
from flask import Flask, request
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from prometheus_client import make_wsgi_app, Counter, Histogram, Info
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import time

db = SQLAlchemy()
login_manager = LoginManager()

# Define Prometheus metrics
REQUEST_COUNT = Counter(
    'flask_request_count', 
    'App Request Count',
    ['method', 'endpoint', 'http_status']
)

REQUEST_LATENCY = Histogram(
    'flask_request_latency_seconds',
    'Request latency',
    ['method', 'endpoint']
)

APP_INFO = Info('flask_app_info', 'Application information')

def before_request():
    request.start_time = time.time()

def after_request(response):
    if hasattr(request, 'start_time'):
        request_latency = time.time() - request.start_time
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.endpoint
        ).observe(request_latency)
    
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.endpoint,
        http_status=response.status_code
    ).inc() 
    
    return response

def create_app():
    app = Flask(__name__)

    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)

    # Add Prometheus wsgi middleware
    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
        '/metrics': make_wsgi_app()
    })

    # Set basic app info
    APP_INFO.info({
        'version': '1.0.0',
        'environment': environment_configuration
    })

    # Register before/after request handlers
    app.before_request(before_request)
    app.after_request(after_request)

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Register blueprints
        from .user_api import user_api_blueprint
        app.register_blueprint(user_api_blueprint)
        return app
