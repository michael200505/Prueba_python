from fastapi import FastAPI
from app.infrastructure.db import init_db
from app.presentation.vehiculo_router import router

app = FastAPI(title="Matrícula Vehicular")
init_db()
app.include_router(router)
