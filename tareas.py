class Tarea:
    def __init__(self, curso, fecha_limite, proceso) -> None:
        self.curso=curso
        self.fecha_limite=fecha_limite
        self.proceso=proceso
    
    def __repr__(self):
        return f"Tarea: curso => {self.name}, fecha límite => {self.code}, proceso => {self.price}"
    
class CrearTareas(Tarea):
    def __init__(self):
        self.tareas = []

    def crear(self, curso, fecha_limite, proceso):
        tarea = Tarea(curso, fecha_limite, proceso)
        self.tareas.append(tarea)
