#!/usr/bin/env python
import time
import pika

credentials = pika.PlainCredentials('admin', 'demo123')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))

channel = connection.channel()

#channel.queue_declare(queue='essocial_param')
channel.queue_declare(queue='essocial_param', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def callback_two(ch, method, properties, body):
    print(" [x] Received %r" % body)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
#channel.basic_consume(callback, queue='hello', no_ack=True)
channel.basic_consume(queue='hello', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()