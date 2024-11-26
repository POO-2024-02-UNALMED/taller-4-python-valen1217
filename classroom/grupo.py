from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"  # Valor inicial de grado según el test

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas is not None else []
        self.listadoAlumnos = estudiantes if estudiantes is not None else []

    def listadoAsignaturas(self, **kwargs):
        """Método para agregar asignaturas al grupo."""
        for nombre in kwargs.values():
            self._asignaturas.append(Asignatura(nombre))

    def agregarAlumno(self, alumno, lista=None):
        """Método para agregar uno o más alumnos al grupo."""
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos += lista

    def __str__(self):
        """Método para representar al grupo y su listado de estudiantes."""
        return f"Grupo de estudiantes: {self._grupo}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        """Método para asignar un nuevo nombre al grado."""
        cls.grado = nombre