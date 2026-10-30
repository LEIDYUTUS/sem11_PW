from fastapi import FastAPI
from .apis.estudiante_api import rutasEstudiantes

app = FastAPI()


app.include_router(rutasEstudiantes, prefix='/api')