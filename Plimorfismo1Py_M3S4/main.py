from libro import Libro

# Crear instancias de la clase Libro
libro_1 = Libro('Dan Brown', 'Inferno')
libro_2 = Libro('Dan Brown', 'The Da Vinci Code', 2003)

# Imprimir los diccionarios de los objetos usando __dict__
print(libro_1.__dict__)  # {'author': 'Dan Brown', 'title': 'Inferno'}
print(libro_2.__dict__)  # {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}
