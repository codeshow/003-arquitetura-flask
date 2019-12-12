from pydaria.ext.database import db


def init_app(app):

    @app.cli.command()
    def createdb():
        """Creates sqlite database"""
        db.create_all()
