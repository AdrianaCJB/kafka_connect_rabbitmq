#!/usr/bin/env python3
import pika
import json
import time

## CREDENCIALES Y CONEXION A RABBITMQ
credentials = pika.PlainCredentials('axity', 'axity')
parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue = 'actividad'
channel.queue_declare(queue = queue, auto_delete=False, durable=True)

properties = pika.BasicProperties(content_type='application/json', delivery_mode=1, priority=1, content_encoding='utf-8')



#### LECTURA DEL ARCHIVO DE DATOS REALES
filename        = 'actividades.csv'
archivo         = open(filename, encoding="utf8",errors='ignore')
textoArchivo    = archivo.read()
lines           = textoArchivo.splitlines();

i = 0
for line in lines:
    i += 1
    line = line.replace('"','')
    list_line = line.split(';')


    msgBody = {
      "nombre":list_line[0],
      "unidad":list_line[1],
      "imei":list_line[2],
      "id":list_line[3],
      "idActividad":list_line[4],
      "codigoActividad":list_line[5],
      "fechaRecepcion":list_line[6], 
      "fechaActividad":list_line[7],  
      "gpsId":list_line[8], 
      "gpsValid":list_line[9],
      "latitud":list_line[10],
      "longitud":list_line[11],
      "velocidadActual":list_line[12],
      "velocidadMaxima":list_line[13],
      "ubicacion":list_line[14],
      "distanciaRecorrida":list_line[15],
      "distanciaAcumulada":list_line[16],
      "nroSatelites":list_line[17],
      "hdop":list_line[18],
      "odometro":list_line[19],
      "horasMotor":list_line[20],
      "idvehiculo":list_line[21],
      "idConductor":list_line[22],
      "altura":list_line[23],
      "heading":list_line[24],
      "idProveedor":list_line[25],
      "ignicion":list_line[26],
      "actividadExtendidaTipo":list_line[27],
      "actividadExtendidaValor":list_line[28],
      "flota":list_line[29],
      "rutConductor":list_line[30],
      "nombreConductor":list_line[31],
      "apellidoPaternoConductor":list_line[32],
      "apellidoMaternoConductor":list_line[33],
      "conductorGrupoId":list_line[34],
      "flotaId":list_line[35],
      "vehiculoEtiquetaID":list_line[36],
      "etiquetaVehiculo":list_line[37],
      "tipoZonaID":list_line[38],
      "nombreZona":list_line[39],
      "clienteId":list_line[40],
      "grupoNombre":list_line[41]
    }

    jsonStr = json.dumps(msgBody)
    properties.message_id = str(i)
    channel.basic_publish(exchange = '', routing_key = queue, body = jsonStr, properties = properties)
    time.sleep(1)

connection.close()
print('Exiting')



## HAY CAMPOS QUE AGREGUÉ QUE NO ESTABAN EN EL JSON QUE ENVIARON POR CORREO PERO SI EN EL ARCHIVO.
## CAMPOS QUE NO VIENEN EN EL ARCHIVO

#"fechaIntegracionInicio":list_line[],
#"rutCliente":list_line[],
#"rutConductor":list_line[],
#"patente":list_line[]
# "idGeocerca":list_line[],