from flask import Flask
from flask.cli import AppGroup


def register_cli(app: Flask):
    datab = AppGroup('datab')

    @datab.command()
    def create():
        from . import db
        db.create_all()

    app.cli.add_command(datab)
