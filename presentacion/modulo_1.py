from tkinter.messagebox import RETRY
from logica.modulo_1 import crear_equipo, consultar_equipo_por_id
from terminaltables import AsciiTable

def crear_equipo_user(conexion):
    
    crear_equipo(conexion,)

def consultar_equipo_por_id_user(conexion):
    id_equipo = input('Ingrese el número del equipo: ')
    respuesta_consulta = consultar_equipo_por_id(conexion, id_equipo)
    if len(respuesta_consulta) == 0:
        print(f'No se ha encontrado el equipo número {id_equipo}')
    else:
        equipo = [list(equipo) for equipo in respuesta_consulta]
        encabezados_de_la_tabla = [['Número de equpio', 'Nombre', 'País', 'Director', 'Marca de bicicleta', 'Marca de ciclocomputador','Dirección de sede central', 'Teléfono', 'Correo electrónico']]
        datos_de_la_tabla = encabezados_de_la_tabla + equipo
        tabla_equipo = AsciiTable(datos_de_la_tabla)
        tabla_equipo.title = ' Consulta de equipos '
        print(tabla_equipo.table)

