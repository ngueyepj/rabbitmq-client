#/usr/bin/env python
import pika


#connecting to pika
credentials = pika.credentials.PlainCredentials('guest', 'a09d8en2o0_d', )
connection = pika.BlockingConnection(pika.ConnectionParameters('3.80.207.210',
                                                               5672,
                                                               '/',
                                                               credentials))
channel = connection.channel()



#creating the excahnge
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

#creating random queues
result = channel.queue_declare(queue='', exclusive=True)
queue_name= result.method.queue

#binding exchange and queues
channel.queue_bind(exchange='logs', queue=queue_name)

def callback(ch, method, properties, body):
    print("[x] recieved %r" % body)

#specify from which queue the message should come
channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)
#endless loop for callbacks
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()