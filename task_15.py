from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# first_method
metadata = MetaData()

products = Table('products', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('name', String(100)),
                     Column('price', Integer),
                     Column('quantity', Integer),
                     Column('comment', String(250))
                    )

engine = create_engine("sqlite:///task_15.sqlite",echo=True)

conn = engine.connect()
pr = products.insert().values(name = 'Cheese', price = 30, quantity = 150, comment = 'Mozzarella')
conn.execute(pr)
pr2 = products.insert().values(name = 'Tomato', price = 10, quantity = 460, comment = 'Foreign')
conn.execute(pr2)
pr3 = products.insert().values(name = 'Milk', price = 5, quantity = 50, comment = 'Nature')
conn.execute(pr3)
pr4 = products.insert().values(name = 'Chocolate', price = 15, quantity = 900, comment = 'Tablerone')
conn.execute(pr4)
s = products.select().where(products.c.id > 2)
result = conn.execute(s)

for row in result:
   print (row)

up = products.update().where(products.c.id == 1).values(comment='Blue')
conn.execute(up)
de = products.delete().where(products.c.id == 3)
conn.execute(de)

#second_method---------------------------------
engine = create_engine("sqlite:///task_15.sqlite",echo=True)
base = declarative_base()
class Product(base):
    __tablename__ = 'products'
    id = Column(primary_key=True)
    name = Column(String(50))
    price = Column(Integer)
    quantity = Column(Integer)
    comment = Column(String(250))

def __init__(self, name, price, quantity, comment):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.comment = comment

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.add_all([Product('Cheese', 30, 150, 'Mozzarella'), Product('Tomato',10, 460, 'Foreign'),
                 Product('Milk', 5, 50, 'Nature'), Product('Chocolate',15, 900, 'Tablerone')])


new_prod = Product('Meet', 35, 20, 'Stake')
session.add(new_prod)
session.commit()

s = session.query(Product).filter_by(name = 'Tomato').first()
if s is None:
    raise Exception('not found')
print(s)
for name, price, quantity, comment in session.query(Product.name, Product.price, Product.quantity, Product.comment,):
    print(name, price, quantity, comment)

for user in session.query(Product).\
         filter(Product.id == 1).\
          filter(Product.price == 30):
   print(user)

new_ = session.query(Product).filter_by(id=2).one()
new_.name = 'ice-cream'
session.add(new_)
session.commit()

re = session.query(Product).filter_by(id=3).one()
re.delete(re)
session.commit()