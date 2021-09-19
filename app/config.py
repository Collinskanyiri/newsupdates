class Config:
    """
    General configuration parent class
    """
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'

    EVERYTHING_SOURCE_API_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'


class ProdConfig(Config):
 pass


class DevConfig(Config):
 DEBUG = True
