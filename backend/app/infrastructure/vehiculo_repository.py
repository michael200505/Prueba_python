from sqlalchemy.orm import Session
from .db import VehiculoTable
from app.domain.vehiculo import Vehiculo

class VehiculoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, v: Vehiculo) -> Vehiculo:
        row = VehiculoTable(**v.__dict__)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return Vehiculo(**row.__dict__)

    def list_all(self) -> list[Vehiculo]:
        rows = self.db.query(VehiculoTable).all()
        return [Vehiculo(**r.__dict__) for r in rows]

    def get_by_placa(self, placa: str) -> Vehiculo | None:
        r = self.db.query(VehiculoTable).filter(VehiculoTable.placa == placa).first()
        return Vehiculo(**r.__dict__) if r else None
