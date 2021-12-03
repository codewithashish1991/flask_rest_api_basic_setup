'''
Inspired by https://www.codementor.io/@mide/how-to-build-restful-apis-with-python-and-flask-fh5x7zjrx
Test by: Ashish KB
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

def create_app(config_filename):
	app = Flask(__name__)
	app.config.from_object(config_filename)

	from urls import api_bp
	app.register_blueprint(api_bp, url_prefix = '/api')
	db.init_app(app)

	return app

if __name__ == '__main__':
	app = create_app("config")
	app.run(host = '127.0.0.1', port=8080, debug=True)
