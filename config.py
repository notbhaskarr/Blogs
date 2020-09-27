import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'oduol'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blogs'
    SQLALCHEMY_TRACK_MODIFICATIONS =True


    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/blogs'

    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,

}
