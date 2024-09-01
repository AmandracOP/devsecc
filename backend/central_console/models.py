from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import Config

Base = declarative_base()
engine = create_engine(Config.DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

class FirewallPolicy(Base):
    __tablename__ = 'firewall_policies'

    id = Column(Integer, primary_key=True)
    app_name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    protocol = Column(String, nullable=False)
    action = Column(String, nullable=False)  # Allow or Block

class NetworkLog(Base):
    __tablename__ = 'network_logs'

    id = Column(Integer, primary_key=True)
    app_name = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    protocol = Column(String, nullable=False)
    packet_size = Column(Integer, nullable=False)
    is_anomalous = Column(Boolean, default=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

# Create all tables
Base.metadata.create_all(engine)
