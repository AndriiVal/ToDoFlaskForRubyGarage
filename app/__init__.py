from flask import Flask

from config import Config
from app.blueprints.main import main as main_blueprint
from app.blueprints.auth import auth as auth_blueprint
from app.extensions import db, migrate, login
from app import models

def create_app():
	app = Flask(__name__)
	app.config.from_object(Config)

	register_extensions(app)

	app.register_blueprint(main_blueprint)
	app.register_blueprint(auth_blueprint, url_prefix="/auth")

	register_make_shell_context(app)

	return app

def register_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db=db)
	login.init_app(app)

def register_make_shell_context(app):
	@app.shell_context_processor
	def make_shell_context():
		return {'db': models.db, 'Users': models.Users, 'Tasks': models.Tasks, 'Projects':models.Projects}