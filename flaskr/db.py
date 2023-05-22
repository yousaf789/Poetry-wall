from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model
from flask import current_app, g
import click
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        g.db = db

    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.session.remove()

def init_db():
    db = get_db()

    db.create_all()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    db.init_app(app)

    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

    with app.app_context():
        db.create_all()
    # db.init_app(app)

# def init_db(app):
#     db.init_app(app)
    # with app.app_context():
    #     db.create_all()