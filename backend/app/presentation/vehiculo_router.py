from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.infrastructure.db import SessionLocal
from app.infrastructure.vehiculo_repository import VehiculoRepository
from app.application.vehiculo_service import VehiculoService
from app.schemas.vehiculo_schemas import VehiculoIn, VehiculoOut
from app.domain.vehiculo import Vehiculo

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=VehiculoOut)
def crear(dto: VehiculoIn, db: Session = Depends(get_db)):
    service = VehiculoService(VehiculoRepository(db))
    return service.registrar(Vehiculo(**dto.model_dump()))

@router.get("", response_model=list[VehiculoOut])
def listar(db: Session = Depends(get_db)):
    service = VehiculoService(VehiculoRepository(db))
    return service.listar()

@router.get("/{placa}", response_model=VehiculoOut)
def obtener(placa: str, db: Session = Depends(get_db)):
    service = VehiculoService(VehiculoRepository(db))
    return service.buscar(placa)
