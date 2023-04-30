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

def calculate_grade(practica_01, practica_02, practica_03, examen, recuperacion, actitud):
    '''
    La función recibirá las notas de todos los apartados evaluados de cada alumno/a
    y devolverá una nota final y un valor Verdadero/Falso en función de si ha aprobado o suspendido.
    :param practica_01: Nota de la práctica 1
    :param practica_02: Nota de la práctica 2
    :param practica_03: Nota de la práctica 3
    :param examen: Nota del examen
    :param recuperacion: Nota de la recuperación
    :param actitud: Nota de actitud
    :return: Nota final y True si es mayor o igual a 5 o False en caso de ser menor que 5
    '''
    nota_final = (practica_01 + practica_02 + practica_03)/3 * 0.3 + max((examen, recuperacion)) * 0.6 + actitud * 0.1
    return round(nota_final, 2), nota_final >= 5

process_class("class.csv")

correos = []
for alumno in alumnado:
    correos.append(create_email(alumno["Nombre"], alumno["Apellido"]))

print(correos)


