from dataclasses import dataclass

@dataclass
class Vehiculo:
    placa: str
    propietario: str
    marca: str
    fabricacion: int
    valor_comercial: float
    impuesto: float = 0.0
    codigo_revision: str = ""
