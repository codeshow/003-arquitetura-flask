from dynaconf import FlaskDynaconf


def init_app(app, **config):
    FlaskDynaconf(app, **config)
