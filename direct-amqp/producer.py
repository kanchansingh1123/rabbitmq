# https://pika.readthedocs.io/en/stable/

# Pika is a pure-Python implementation of the AMQP 0-9-1 protocol

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue="hello")

channel.basic_publish(exchange="", routing_key="hello", body="Hello Dev!")
channel.basic_publish(exchange="", routing_key="hello", body="Hello Moto!")
print("[x] Sent Hello World")

connection.close()