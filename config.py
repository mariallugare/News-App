import os

class Config:
    
    NEWS_API_BASE_URL = 'https://newsapi.org/v2'
    NEWS_API_KEY = 'd4f3a1944f534b2b962ebe231208abd2'
    SECRET_KEY = '0000'
    NEWS_API_SOURCE_URL = 'https://newsapi.org/v2/sources?apiKey={}'.format(NEWS_API_KEY)
    NEWS_API_ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}