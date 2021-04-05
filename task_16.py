from sqlalchemy import create_engine, ForeignKey, update
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("postgresql://postgres:postgres@localhost/test",echo = True)
Base = declarative_base()


class Car(Base):
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True)
    model = Column(String(255))
    release_year = Column(Integer)
    brand_id = Column(Integer,ForeignKey('brand.id'),nullable=False)

    brand = relationship('Brand_car',foreign_keys ='Car.brand_id',backref ='cars')

    def __init__(self, model, release_year, brand_id):
        self.model = model
        self.release_year = release_year
        self.brand_id = brand_id

class Brand_car(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


    def __init__(self, name):
        self.name = name

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
name_car1 = Brand_car('BMW')
name_car2 = Brand_car('Audi')
name_car3 = Brand_car('Mercedes')
name_car4 = Brand_car('Porsche')
character1 = Car('M5',2018,5)
character2 = Car('S5',2015,3)
character3 = Car('E63s',2019,2)
character4 = Car('Panamera turbo 4S',2017,1)
session.add_all([name_car1,name_car2,name_car3,name_car4])
session.add_all([character1,character1,character3,character4])
session.commit()

car = session.query(Brand_car).filter_by(name="BMW").all()
if car is None:
    raise Exception('not found')
print(car)

for model, release_year, brand_id in session.query(Car.model, Car.release_year, Car.brand_id,):
    print(f'{model}:{release_year}:{brand_id}')

for c in session.query(Car).filter(Car.id == 1).filter(Car.release_year >= 2015):
   print(c)

new_car = session.query(Brand_car).filter_by(id=2).one()
new_car.name = 'Volvo'
session.add(new_car)
session.commit()


refound = session.query(Brand_car).filter_by(id=3).one()
refound.delete(refound)
session.commit()