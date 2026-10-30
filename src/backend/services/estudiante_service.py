from ..repositories.estudiante_repository import EstudianteRepositorio
from ..schemas.estudiante import Estudiante, EstudianteActualizar

class EstudianteServicio:
    def __init__(self):
            self.__estudianteRepositorio = EstudianteRepositorio()
    def guardarEstudiante(self, estudianteNuevo: Estudiante ):
          try:
            return self.__estudianteRepositorio.guardarEstudiante(estudianteNuevo)
          except Exception as e:
               raise str(e)
    def mostrarEstudiante(self):
          return self.__estudianteRepositorio.mostrarEstudiante()

    def actualizarEstudiante(self, id:int, estudianteActualizar: EstudianteActualizar):
          try:               
            return self.__estudianteRepositorio.actualizarEstudiantes(id, estudianteActualizar)
          except Exception  as e:
               raise str(e)
               
    def eliminarEstudiante(self, id:int):
          try:
            return self.__estudianteRepositorio.eliminarEstudiante(id)
          except Exception as e:
            raise str(e)