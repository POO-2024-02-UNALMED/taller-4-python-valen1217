from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 6" 

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos.extend(lista) 

    def listadoAsignaturas(self, *nombres_asignaturas):
        for nombre in nombres_asignaturas:
            self._asignaturas.append(Asignatura(nombre))  

    def __str__(self):
        alumnos_str = ", ".join(self.listadoAlumnos)
        return f"Grupo de estudiantes: {self._grupo} ({alumnos_str})"

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre