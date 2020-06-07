#!usr/bin/env python
import pika



#establishing Connection with RabbitMQ
credentials = pika.credentials.PlainCredentials('guest', 'a09d8en2o0_d', )
connection = pika.BlockingConnection(pika.ConnectionParameters('3.80.207.210',
                                                               5672,
                                                               '/',
                                                               credentials))
channel = connection.channel()

#create exchange using exchange_declare for send_Message
channel.exchange_declare(exchange='topic_logs',
                         exchange_type='topic')

#publishing to named exchange in exchange
channel.basic_publish(exchange='topic_logs',
                      routing_key='',
                      body='Hello World')
print(" [x] sent 'Hello World! then severity'")

#creating random queues using queue_declare queue deleted after closing connection
#channel.queue_declare(queue='', exclusive=True)


#closing connection
connection.close()



