from sqlalchemy.orm import Session
from .db import VehiculoTable
from app.domain.vehiculo import Vehiculo

class VehiculoRepository:
    def __init__(self, db: Session):
        self.db = db

    def _to_domain(self, r: VehiculoTable) -> Vehiculo:
        return Vehiculo(
            placa=r.placa,
            propietario=r.propietario,
            marca=r.marca,
            fabricacion=r.fabricacion,
            valor_comercial=r.valor_comercial,
            impuesto=r.impuesto,
            codigo_revision=r.codigo_revision,
        )

    def create(self, v: Vehiculo) -> Vehiculo:
        row = VehiculoTable(**v.__dict__)
        self.db.add(row)
        self.db.commit()
        self.db.refresh(row)
        return self._to_domain(row)

    def list_all(self) -> list[Vehiculo]:
        rows = self.db.query(VehiculoTable).all()
        return [self._to_domain(r) for r in rows]

    def get_by_placa(self, placa: str) -> Vehiculo | None:
        r = self.db.query(VehiculoTable).filter(VehiculoTable.placa == placa).first()
        return self._to_domain(r) if r else None


