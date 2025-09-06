from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from flask_migrate import Migrate
from config import Config
from extensions import db, ma

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    CORS(app)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)  

    # Import models so Alembic knows them
    with app.app_context():
        from models.user import User
        from models.incident import Incident
       

    # Swagger
    SWAGGER_URL = "/api/v1/docs"
    API_URL = "/static/swagger.json"
    swagger_bp = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)

    # Blueprints
    from routes.user_routes import user_bp
    from routes.incident_routes import incident_bp
    app.register_blueprint(user_bp, url_prefix="/api/v1/users")
    app.register_blueprint(incident_bp, url_prefix="/api/v1/incidents")

    @app.route("/api/v1/")
    def index():
        return {"message": "MediSafe Tracker API v1 is running 🚀"}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
