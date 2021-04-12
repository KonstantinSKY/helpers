from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

DB_NAME = 'am2'
DB_USER = 'sky'
DB_PASSW = ''

# engine = create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASSW}@localhost/{DB_NAME}')

engine =  create_engine(f'sqlite:///{DB_NAME}.db', echo=True)
Base = declarative_base()

#-----------------------------------------------------
# Table `Continents`
#-----------------------------------------------------
class Continents(Base):
    __tablename__ = 'Continents'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    code = Column(String(2), unique=True)
    countries = relationship("Countries")

# -----------------------------------------------------
# -- Table `Countries`
# -----------------------------------------------------
class Countries(Base):
    __tablename__ = 'Countries'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False, unique=True)
    code = Column(String(2), unique=True)
    continent_id = Column(Integer,ForeignKey('Continents.id'))



if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # print(Quotes.__tablename__)
#class Groups(Base):
 #   __table__ = Table("groups", Base.metadata, autoload_with=engine)



# engine.connect()
#print(engine.table_names())
#sess = sessionmaker(bind=engine)()
#print(sess)
#print(sess.query(Groups))
#print(Groups.__table__.columns.keys())
#print(Groups.query.first())
