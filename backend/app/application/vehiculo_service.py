from fastapi import HTTPException
from app.domain.vehiculo import Vehiculo
from app.infrastructure.vehiculo_repository import VehiculoRepository

class VehiculoService:
    def __init__(self, repo: VehiculoRepository):
        self.repo = repo

    def registrar(self, v: Vehiculo) -> Vehiculo:
        if len(v.placa) < 4 or v.placa[3] != "-":
            raise HTTPException(status_code=400, detail="La placa debe tener '-' en la cuarta posición.")

        base = 0.025 * v.valor_comercial
        if v.fabricacion < 2010:
            base += 0.10 * base

        if v.marca and v.marca[0].lower() in "aeiou":
            base -= 30.0

        v.impuesto = max(0.0, float(base))
        v.codigo_revision = f"{v.placa[:3]}{len(v.propietario)}{str(v.fabricacion)[-1]}"
        return self.repo.create(v)

    def listar(self):
        return self.repo.list_all()

    def buscar(self, placa: str):
        v = self.repo.get_by_placa(placa)
        if not v:
            raise HTTPException(status_code=404, detail="Vehículo no encontrado.")
        return v
