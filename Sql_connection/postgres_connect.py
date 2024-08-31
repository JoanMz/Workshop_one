from decouple import config
from datetime import datetime
from sqlalchemy import create_engine
from logging import Logger

logger = Logger(name='log', level=20)

def connection():
    try:
        engine = create_engine(f"postgresql://{config("DB_USER")}:{config("DB_PASSWORD")}@{config("DB_HOST")}/{config("DB_DATABASE")}")
        logger.log(level=20, msg=f'DB_ENGINE Charge {datetime.now()}')
        return engine
    except:
        logger.log(level=40, msg='An error ocurre')
        return None
        

    