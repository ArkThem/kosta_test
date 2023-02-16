from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bd import Service, PriceList

engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()

services_and_prices = session.query(Service.service_name, PriceList.price).join(PriceList).all()

for service, price in services_and_prices:
    print(service, price)
