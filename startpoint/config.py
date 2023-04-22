from .constants import DATABASE_FILE_NAME


class AppConfig:
    SECRET_KEY = '61bce5146d4449d6e442eeea4286d7d015d618ffb9a844d34960f2cd14bc142e'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_FILE_NAME}'