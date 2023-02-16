from sqlalchemy import create_engine, Column, Integer, String, Text, DECIMAL, Date, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://username:password@localhost/db_name')

Base = declarative_base()

class Service(Base):
    __tablename__ = 'services'

    service_id = Column(Integer, primary_key=True)
    service_name = Column(String(255))
    service_description = Column(Text)

    prices = relationship("PriceList", back_populates="service")


class PriceList(Base):
    __tablename__ = 'price_list'

    price_id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('services.service_id'))
    price = Column(DECIMAL(10,2))
    date_from = Column(Date)
    date_to = Column(Date)

    service = relationship("Service", back_populates="prices")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()