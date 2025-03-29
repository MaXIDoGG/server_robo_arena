from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Движок — это как "ключ зажигания" для работы с БД
engine = create_engine("sqlite:///data.db")

# Сессии (подробнее в следующем разделе)
Session = sessionmaker(bind=engine)
session = Session()

# BaseModel — шаблон для всех моделей
BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    phone = Column(String(100), unique=True, index=True)
    password = Column(String(100))

    def __repr__(self):
        return f"<Пользователь: {self.title}, {self.password}>"


BaseModel.metadata.create_all(engine)
