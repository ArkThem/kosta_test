from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bd import Service, PriceList

engine = create_engine('mysql+pymysql://username:password@localhost/db_name')
Session = sessionmaker(bind=engine)
session = Session()

new_service = Service(service_name='УЗИ органов брюшной полости', service_description='Диагностика заболеваний органов брюшной полости при помощи ультразвука')
session.add(new_service)
session.commit()

new_price = PriceList(service_id=new_service.service_id, price=1200, date_from=date.today(), date_to=None)
session.add(new_price)
session.commit()
