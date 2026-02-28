from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register blueprints
    from .routes.main_routes import main_bp
    from .routes.product_routes import product_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)

    return app