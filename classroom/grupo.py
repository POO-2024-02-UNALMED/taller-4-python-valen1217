from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 6"  # Valor inicial

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def agregarAlumno(self, alumno):
        """Agrega un alumno al listado de alumnos del grupo."""
        self.listadoAlumnos.append(alumno)

    def listadoAsignaturas(self, *nombres_asignaturas):
        """Añade asignaturas con los nombres proporcionados."""
        for nombre in nombres_asignaturas:
            self._asignaturas.append(Asignatura(nombre))  # Añadimos asignaturas con los nombres

    def __str__(self):
        alumnos_str = ", ".join(self.listadoAlumnos)
        return f"Grupo de estudiantes: {self._grupo}"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre