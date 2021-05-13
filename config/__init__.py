import os


class Config:
    DATABASE_URI = os.environ["DATABASE_URI"]
    USERNAME = os.environ["SKYPE_USERNAME"]
    PASSWORD = os.environ["SKYPE_PASSWORD"]
    COMMAND_PREFIX = os.environ.get("COMMAND_PREFIX", "!")


class Development(Config):
    ENV = "dev"


class Production(Config):
    ENV = "prod"


env = os.environ.get("ENV", "dev")
config = Production if env == "prod" else Development
