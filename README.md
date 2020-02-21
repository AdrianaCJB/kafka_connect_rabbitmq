# kafka_connect_rabbitmq

#### Nota: Se asume que está instalado previamente Java 8, Confluent Platform el cual contiene (Zookeeper, Kafka, conectores bases para standalone y distributed) y aparte el conector a RabbitMQ. 

```>> wget http://packages.confluent.io/archive/5.4/confluent-5.4.0-2.12.tar.gz```

```>> wget http://client.hub.confluent.io/confluent-hub-client-latest.tar.gz```

```>> confluent-hub install confluentinc/kafka-connect-rabbitmq:latest```

#### Haber creado el topic en Kafka que reciba los mensajes desde la carpeta de Confluent:

```>> ./bin/kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic actividad_topic ```

#### La idea de este ejercicio es tener Rabbitmq en un Docker y que envíe mensajes a un cluster Kafka en otro servidor.


### Archivos:

**1. src/actividades.csv:** Archivo con datos reales de actividades


**2. docker-compose.yml :** Crea en docker un contenedor de rabbitmq

Al crear el contenedor se debe entrar y crear la cola:

```>> docker exec -it rabbitmq bash```

```>> curl --user user:pass -X PUT -H 'content-type: application/json' --data-binary '{"vhost":"/","name":"actividad","durable":"true","auto_delete":"false","arguments":{"x-queue-type":"classic"}}' 'http://localhost:15672/api/queues/%2F/actividad'```


**3. producer_rabbitmq.py :** Proceso que lee un archivo de "actividades.csv" y envía cada 1 segundo linea por linea los mensajes a la cola de rabbitmq llamada "actividad" en formato JSON.

**4. config/RabbitMQSourceConnector.properties:**  Archivo que está dentro del servidor de kafka y contiene las configuraciones del RabbitMQ a consumir. 


