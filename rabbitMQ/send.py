#!/usr/bin/env python
import sys
import pika

from Queue import Queue

credentials = pika.PlainCredentials('admin', 'demo123')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', credentials=credentials))
channel = connection.channel()

#channel.queue_declare(queue='essocial_param')
channel.queue_declare(queue='essocial_param', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
  exchange='',
  routing_key='hello',
  body=message,
  properties=pika.BasicProperties(
    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
  ))

print(" [x] Sent %r" % message)

connection.close()


defaults = {
  'server' : {
      'host': 'localhost',
      'port': 5672,
      'user': 'admin',
      'pass': 'demo123',
  },

      'queue': {
          'passive': False,
          'durable': True,
          'exclusive': False,
          'autoDelete': False,
          'nowait': False
      },
      'consumer': {
          'noLocal': False,
          'noAck': False,
          'exclusive': False,
          'nowait': False
      }
}

#c = Queue("hello1", defaults)
#c.emit(["11", "aaaa"])