from __future__ import annotations
from urllib.parse import quote_plus
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class SqlAlchemyBuilder:
    def __init__(self, server: str, database: str):
        self.server = server
        self.database = database
        self.user = os.getenv('MYSQL_USER')
        self.password = quote_plus(os.getenv('MYSQL_PASSWORD'))
        self.port = os.getenv('MYSQL_PORT')

        print(self.user)
        print(self.password)

        self.sql_alchemy_url = (
            f"mysql+pymysql://{self.user}:{self.password}@{self.server}:{self.port}/{self.database}"
            f"?charset=utf8mb4"
        )
        self.engine = create_engine(self.sql_alchemy_url, pool_pre_ping=True)
        self.session_local = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def get_session(self):
        return self.session_local