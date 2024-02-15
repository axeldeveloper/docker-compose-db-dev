#!/usr/bin/env python
import json
import time
import pika


user = "admin"
pwd  = "demo123"
host = "localhost"
port = ""

exchange_name = 'holerite_exchange'
routing_key = 'holerite_key'
queue_name = 'holerite_queue'

credentials = pika.PlainCredentials(user, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,port='5672',credentials=credentials))

channel = connection.channel()

# Declara o exchange e a fila, se não existirem
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

#channel.queue_declare(queue='essocial_param', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback_two(ch, method, properties, body):
    # print(" [x] Received %r" % body)
    dados = json.loads(body)
    print(f"Recebida solicitação de orçamento para {dados['pfis_numero']}")
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def callback(ch, method, properties, body):
    print(" [x] solicitação recebida %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


# channel.basic_qos(prefetch_count=1)
# channel.basic_consume(callback, queue='hello', no_ack=True)


# Define o callback para processar as mensagens recebidas
# channel.basic_consume(queue='essocial_param', on_message_callback=callback)
channel.basic_consume(queue=queue_name, on_message_callback=callback_two, auto_ack=False)


#print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()