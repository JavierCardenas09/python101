import csv
#Leer CSV
def leer_csv():
    path_archivo = 'Data/empleados.csv'

    with open(path_archivo) as csv_file:
        reader = csv.reader(csv_file)
        lector = reader
        for linea in lector:
            print(linea)

#leer como diccionario
def leer_csv_dict():
    ruta_archivo = 'Data/empleados.csv'

    with open(ruta_archivo,'r') as csv_archivo:
        reader1 = csv.DictReader(csv_archivo)
        lector1 = reader1
        for linea1 in lector1:
            print(linea1)

#Llamado de funcion
if __name__ == '__main__':
    leer_csv_dict()
#    leer_csv()

