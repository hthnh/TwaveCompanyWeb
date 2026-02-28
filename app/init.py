from flask import Flask

from .content_store import load_site_content


def create_app():
    app = Flask(__name__)

    @app.context_processor
    def inject_site_content():
        # Reload each request so edits in site.json appear immediately.
        return {"site": load_site_content(app.root_path)}

    # Register blueprints
    from .routes.main_routes import main_bp
    from .routes.product_routes import product_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp)

    return app
