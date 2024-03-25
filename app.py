from flask import Flask, jsonify
from extensions import db, migrate
from models import *  # Import models to ensure they are registered with SQLAlchemy
from crud_ops import crud  # Import the blueprint for your CRUD operations

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    app.register_blueprint(crud, url_prefix='/api')  # Register the CRUD blueprint

    # Error handlers
    def error_response(status_code, message):
        response = jsonify({'error': message})
        response.status_code = status_code
        return response

    @app.errorhandler(404)
    def not_found_error(error):
        return error_response(404, 'Resource not found')

    @app.errorhandler(400)
    def bad_request_error(error):
        return error_response(400, 'Bad request')

    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()  # In case a database error occurred
        return error_response(500, 'An internal error occurred')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
