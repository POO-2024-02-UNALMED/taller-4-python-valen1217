from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        if asignaturas is None:
            asignaturas = []
        if estudiantes is None:
            estudiantes = []
        
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, asignaturas):
        """Agrega asignaturas a la lista _asignaturas."""
        for asignatura in asignaturas:
            self._asignaturas.append(Asignatura(asignatura))

    def agregarAlumno(self, alumno):
        """Agrega un alumno al listado de alumnos del grupo."""
        self.listadoAlumnos.append(alumno)

    @classmethod
    def asignarNombre(cls, nombre):
        """Asignar un nombre al grado del grupo."""
        cls.grado = nombre