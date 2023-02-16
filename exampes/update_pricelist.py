from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bd import PriceList

engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()

price_to_update = session.query(PriceList).filter(PriceList.price_id == 1).first()
price_to_update.price = 700
price_to_update.date_to = date.today()

session.commit()
