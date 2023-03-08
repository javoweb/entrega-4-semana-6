from pulsar.schema import String, Long, Array


class OrdenCreada:
    id = String()
    nombres = String()
    apellidos = String()
    email = String()
    productos = Array(String())
    fecha_creacion = Long()
