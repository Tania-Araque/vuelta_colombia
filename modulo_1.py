# Módulo 1: Módulo de gestión de equipos inscritos y afiliados
# Importando librerias necesarias para enviar el correo electrónico de los inscritos
import smtplib, ssl
from email.message import EmailMessage

def crear_equipo(conexion, equipo):
  """
  Función creación de equipo.
  Recibe un objeto Connection.
  Recibe una lista de la siguiente manera:
  [num_equipo, pais_sede, director , marca_bicicleta, marca_ciclocomputador,
  direccion_sede_central, telefono, correo_electronico]
  """
  #falta verficar equipo
  cursor              = conexion.cursor()
  sentencia_insercion = 'INSERT INTO equipos(pais_sede, director, marca_bicicleta, marca_ciclocomputador, direccion_sede_central, telefono, correo_electronico) VALUES(?,?,?,?,?,?,?)'
  cursor.execute(sentencia_insercion, equipo)
  conexion.commit()

def consultar_equipo_por_id(conexion, id_equipo):
  """
  Función consulta por número de equipo.
  Recibe un objeto Connection (conexion).
  Recibe el número de equipo a consultar (id_equipo).
  """
  cursor             = conexion.cursor()
  sentencia_consulta = f'SELECT * FROM equipos WHERE num_equipo = {id_equipo}'
  respuesta_consulta = cursor.execute(sentencia_consulta)
  equipo = respuesta_consulta.fetchall()
  return equipo

def cambiar_sede_equipo(conexion, id_equipo, nueva_direccion):
  """
  Función cambio de sede central de un equipo.
  Recibe un objeto Connection (conexion).
  Recibe el número del equipo a modificar (id_equipo).
  Recibe la nueva dirección de sede.
  """
  cursor                  = conexion.cursor()
  sentencia_actualizacion = f'UPDATE equipo SET direccion_sede_central = {nueva_direccion} WHERE num_equipo = {id_equipo}'
  cursor.execute(sentencia_actualizacion)
  conexion.commit()

import smtplib, ssl
from email.message import EmailMessage

def enviar_correo_verificacion(**destinatario):
  """
  Función que envia un correo de verifcación que dice:
  Estimad@ {nombre} {apellido} su inscripcion a La Vuelta Colombia ha sido finalizada con exito.
  Gracias por participar
  Recibe como argumento la dirección del correo del destinatario (destinatario)
  """

  mensaje  = f"""Estimad@ {destinatario['nombre']} {destinatario['apellido']} su inscripcion a La Vuelta Colombia ha sido finalizada con exito.
Gracias por participar"""

  # email que creamos para enviar los correos xd
  remitente              = 'trabajopooxd@gmail.com'
  contrasena_remitente   = 'trabajito poo'
  asunto                 = 'Confirmación inscripción a La Vuelta Colombia.'

  # Se crea un objeto de la clase EmailMessage el cual va a ser enviado por el servidor smtp como mensaje
  correo_electronico            = EmailMessage()
  # Asignando el contenido, asunto, remitente y destinatario al objeto correo_electronico
  correo_electronico.set_content(mensaje)
  correo_electronico['Subject'] = asunto
  correo_electronico['From']    = remitente
  correo_electronico['To']      = destinatario['correo']

  # Variables para ajustes del servidor
  puerto = 465  # For SSL
  servidor_smtp = "smtp.gmail.com"
  contexto = ssl.create_default_context()

  # Creando el servidor y enviando el correo
  with smtplib.SMTP_SSL(servidor_smtp, puerto, context=contexto) as servidor:
        # Iniciando sesión en el servidor
        servidor.login(remitente, contrasena_remitente)
        #Enviando el correo electronico
        servidor.send_message(correo_electronico, from_addr=remitente, to_addrs=destinatario['correo'])
        print(f"Se ha enviado un correo de verificación a {destinatario['nombre']} {destinatario['apellido']} {destinatario['correo']}")