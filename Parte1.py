# Importamos la librería csv que permite trabajar con ficheros csv y convertirlos en un diccionario
import csv
import pprint as pp

# Declaro el diccionario notas con las claves y listas vacías
notas: dict = {
    "Nombre": [],
    "Apellido": [],
    "Practica01": [],
    "Practica02": [],
    "Practica03": [],
    "Examen": [],
    "Recuperacion": [],
    "Actitud": []
}

def process_class(path: str, encoding="UTF-8"):
    """
    Pasa los datos del csv al diccionario

    Args:
        path (str): Ruta del fichero csv
    """
    with open(path) as file:
        # Convierto el fichero csv en un diccionario en el que los valores de cada clave son las claves de la primera línea
        file_dict = csv.DictReader(file)
        # Recorro el diccionario y añade los valores a las listas del diccionario notas
        for line in file_dict:
            notas["Nombre"].append(line["Nombre"])
            notas["Apellido"].append(line["Apellido"])
            # Primero se convierten las comas en puntos para poder convertirlos a float y añadirlos a la lista
            notas["Practica01"].append(float(line["Practica01"].replace(",", ".")))
            notas["Practica02"].append(float(line["Practica02"].replace(",", ".")))
            notas["Practica03"].append(float(line["Practica03"].replace(",", ".")))
            notas["Examen"].append(float(line["Examen"].replace(",", ".")))
            notas["Recuperacion"].append(float(line["Recuperacion"].replace(",", ".")))
            notas["Actitud"].append(float(line["Actitud"].replace(",", ".")))

process_class("class.csv")
print(notas)