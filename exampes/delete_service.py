from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bd import Service, PriceList

engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()

service_to_delete = session.query(Service).filter(Service.service_id == 2).first()
session.delete(service_to_delete)
session.commit()
