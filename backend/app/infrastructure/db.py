from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///matricula.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class VehiculoTable(Base):
    __tablename__ = "vehiculos"
    placa = Column(String, primary_key=True, index=True)
    propietario = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    fabricacion = Column(Integer, nullable=False)
    valor_comercial = Column(Float, nullable=False)
    impuesto = Column(Float, nullable=False)
    codigo_revision = Column(String, nullable=False)

def init_db():
    Base.metadata.create_all(bind=engine)
