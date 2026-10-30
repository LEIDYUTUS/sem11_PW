from fastapi import APIRouter, HTTPException, status
from ..services.estudiante_service import EstudianteServicio
from ..schemas.estudiante import Estudiante, EstudianteActualizar

rutasEstudiantes = APIRouter(prefix= '/estudiantes', tags= ['Estudiantes'])
EstudianteServicio = EstudianteServicio()

@rutasEstudiantes.post('/')
def guardarEstudiante(estudianteNuevo: Estudiante):
    try:
        return EstudianteServicio.guardarEstudiante(estudianteNuevo)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e) )
@rutasEstudiantes.get('/')
def mostrarEstudiante():
    return EstudianteServicio.mostrarEstudiante()

@rutasEstudiantes.put('/{id}')
def actualizarEstudiante(id:int, estudianteActualizar:EstudianteActualizar):
    try:
        return EstudianteServicio.actualizarEstudiante(id, estudianteActualizar)
    except   Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))
@rutasEstudiantes.delete('/{id}')
def eliminarEstudiante(id:int):
    try:
        return EstudianteServicio.eliminarEstudiante(id)
    except   Exception as e:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail= str(e))
    