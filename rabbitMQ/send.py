#!/usr/bin/env python
import json
import sys
import pika


user = "admin"
pwd  = "demo123"
host = "localhost"
port = ""
exchange_name = 'holerite_exchange'
routing_key = 'holerite_key'
queue_name = "holerite_queue"
cloudamqp_url = 'amqps://dsynhobk:bGNUEwey6BpvLfUs9dF5MxL8R72SRvOe@hawk.rmq.cloudamqp.com/dsynhobk'


# Função para gerar orçamento
def gerar_orcamento(dados):
    # Simulação de cálculo de orçamento
    valor = dados['valor'] + (dados['valor'] * 0.1)

    # Retorno do orçamento
    return {
        'valor': valor,
        'moeda': 'BRL',
        'prazo': 10,
        'pfis_numero': dados['pfis_numero']
    }


credentials = pika.PlainCredentials(user, pwd)

connection = pika.BlockingConnection(pika.ConnectionParameters(host=host,port='5672',credentials=credentials))

channel = connection.channel()

# Declaração da fila
channel.queue_declare(queue=queue_name, durable=True)

# Declara o exchange, se não existir
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

message = ' '.join(sys.argv[1:]) or "Holerite!"

pessoa = {
    "valor": 1500,
    'pfis_numero': sys.argv[1:]

}

orcamento = gerar_orcamento(pessoa)

channel.basic_publish(
    exchange=exchange_name,
    routing_key=routing_key,
    # routing_key=properties.reply_to,
    # body=message,
    body=json.dumps(orcamento)
    #properties=pika.BasicProperties(
    #    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
    #)
)

print(" [x] Sent %r" % message)

connection.close()


defaults = {
    'server': {
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

# c = Queue("hello1", defaults)
# c.emit(["11", "aaaa"])
