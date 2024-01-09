from easydict import EasyDict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from util import convertor


class DBConnector:
    def __init__(self, config: dict):
        conf = EasyDict(config)

        self._engine = create_engine(f'mysql+pymysql://{conf.userName}:{conf.password}@{conf.host}:{conf.port}/{conf.database}')

        self._session = scoped_session(sessionmaker(autoflush=False, bind=self._engine))

    def insert_data(self, data_list: list):
        for data in data_list:
            entity = convertor.dto_to_entity(data)
            self._session.add(entity)

        self._session.commit()

    def session_close(self):
        self._session.close()
