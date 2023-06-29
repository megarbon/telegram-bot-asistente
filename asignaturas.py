#una estructura de datos donde almacenamos los datos de las asignaturas como el profesor que las imparte y sus datos

class Asignatura:
    def __init__(self, nombre, profesor, correo):
        self.nombre = nombre
        self.profesor = profesor
        self.correo = correo

movil_asignatura = Asignatura("Desarrollo Movil", "Andres Parra", "andres.parra@educamadrid.es")
servidor_asignatura = Asignatura("Entorno Servidor", "Eva Alonso", "eva.alonso@educamadrid.es")
cliente_asignatura = Asignatura("Entorno Cliente", "Eva Alonso", "eva.alonso@educamadrid.es")

