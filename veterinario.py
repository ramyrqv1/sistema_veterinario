"""------sistema para una vetererinaria--------"""


class Mascota:
    id = 0

    def __init__(self, nombre, tipo_de_animal, raza, edad):
        self._nombre = nombre
        self._tipo_de_animal = tipo_de_animal
        self._raza = raza
        self._edad = edad
        Mascota.id += 1
        self.id = Mascota.id

    def __str__(self):
        return f"ID: {self.id} > {self._nombre} es un {self._tipo_de_animal} y es de raza {self._raza} y tiene {self._edad} años"

    def agregar_mascota():
        nombre_mascota = input("Ingrese el nombre de la mascota: ")
        tipo_mascota = input("Ingrese el tipo de animal: ")
        raza_mascota = input("Ingrese la raza del animal: ")
        edad_mascota = int(input("Ingrese la edad de la mascota: "))
        nueva_mascota = Mascota(
            nombre_mascota, tipo_mascota, raza_mascota, edad_mascota
        )
        # agregar mascotas a la lista
        lista_mascotas.append(nueva_mascota)


# sistema de mascotas
print(
    """Sistema de mascotas elige una opcion:
    1 - Agregar mascota
    2 - Listar mascotas
    0 - Salir del sistema"""
)

opcion = int(input("Opción:"))
lista_mascotas = []

while opcion != 0:
    if opcion == 1:
        Mascota.agregar_mascota()

    elif opcion == 2:
        for mascota in lista_mascotas:
            print(mascota)

    opcion = int(input("Opción:"))

print("Fin del programa de registro de mascotas")
