import csv

alumnado = []
def process_class(ruta):
   """
   Lee los datos y los almacena en una lista de diccionarios donde en cada uno
   de los alumnos las claves serán los datos de la cabecera del archivo CSV
   y los valores serán los datos de cada alumno/a.
   :param ruta: un str con la ruta del fichero (.csv) a abrir.
   :return: None
   """
   global alumnado # He añadido esta linea de código porque sin el global no modificaba la lista alumnado quese encuentra fuera de la función
   alumnado = []
   with open(ruta, newline='', encoding="UTF-8") as csvfile:
       reader = csv.DictReader(csvfile)
       for fila in reader:
           alumnado.append(fila)
   return

def create_email(nombre, apellido):
    """
    Crea un correo electrónico con la primera letra del nombre y con las primeras 5 letras del apellido (Si las hubiera) y el dominio '@educacion.navarra.es'
    :param nombre: Nombre del alumno
    :param apellido: Apellido del alumno
    :return: Un str con el email resultante
    """
    return nombre[0] + (apellido[0:5] if len(apellido) > 5 else apellido) + "@educacion.navarra.es"

process_class("class.csv")

correos = []
for alumno in alumnado:
    correos.append(create_email(alumno["Nombre"], alumno["Apellido"]))

print(correos)
