#!/usr/bin/env python
import pika


#establishing Connection with RabbitMQ
credentials = pika.credentials.PlainCredentials('guest', 'a09d8en2o0_d', )
connection = pika.BlockingConnection(pika.ConnectionParameters('3.80.207.210',
                                                               5672,
                                                               '/',
                                                               credentials))
channel = connection.channel()

#create queue using queue_declare for send_Message
channel.queue_declare(queue='the_queue')

def callback(ch, method, properties, body):
    print("[x] recieved %r" % body)

#specify from which queue the message should come
channel.basic_consume(queue='the_queue',
                      auto_ack=True,
                      on_message_callback=callback)
#endless loop for callbacks
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

