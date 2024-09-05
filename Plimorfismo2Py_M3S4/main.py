class Persona:
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfono: {self.telefono}"

personas = []

persona1 = Persona("Juan", "Pérez", "123456789")
persona2 = Persona("María", "González", "987654321")
persona3 = Persona("Pedro", "Rodríguez", "555555555")

personas.append(persona1)
personas.append(persona2)
personas.append(persona3)

for persona in personas:
    print(persona)