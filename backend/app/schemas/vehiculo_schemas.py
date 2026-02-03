from pydantic import BaseModel

class VehiculoIn(BaseModel):
    placa: str
    propietario: str
    marca: str
    fabricacion: int
    valor_comercial: float

class VehiculoOut(VehiculoIn):
    impuesto: float
    codigo_revision: str


