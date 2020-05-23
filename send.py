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

#specifying queue name in exchange
channel.basic_publish(exchange='',
                      routing_key='the_queue',
                      body='Hello World')
print(" [x] sent 'Hello World!'")

#closing connection
connection.close()

