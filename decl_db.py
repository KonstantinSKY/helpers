from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from datetime import DateTime

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
    created_on = Column(DateTime, default=datetime.now, nullable=False)
#-----------------------------------------------------
# -- Table `Regions`
#-----------------------------------------------------
class Regions(Base):
    __tablename__ = 'Regions'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    code = Column(String(2), unique=True)
    created_on = Column(DateTime, default=datetime.now, nullable=False)
#-----------------------------------------------------
# -- Table `Cities`
#-----------------------------------------------------
class Cities(Cities):
    __tablename__ = 'Cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    created_on = Column(DateTime, default=datetime.now, nullable=False)

#-----------------------------------------------------
# Table Providers
# -----------------------------------------------------
class Providers(Base):
    __tablename__ = 'Providers'
    id = Column(Integer, primary_key=True)
    name_isp = Column(String(30), unique=True)
    as_number = Column(String(10), unique=True)
    as_name = Column(String(60), unique=True)
    organization = Column(String(60), unique=True)
    created = Column(DateTime, default=datetime.now, nullable=False)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=False)





 47 CREATE TABLE IF NOT EXISTS Providers (
 48     id SERIAL PRIMARY KEY,
 49     name_isp VARCHAR(45),
 50     organization VARCHAR(45),
 51     as_number VARCHAR(10),
 52     as_name VARCHAR(45),
 53     created_ts TIMESTAMPTZ DEFAULT NOW()
 54 );
 55 





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
