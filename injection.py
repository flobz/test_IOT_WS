from time import sleep, time_ns

import pika
from pymongo import MongoClient, ASCENDING
import pprint
import psutil
import json
from bson import json_util

parameters = pika.URLParameters('amqp://rabbitmq:rabbitmq@rabbitmq1:5672/')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='laptop_temperature')
while True:
    temp=psutil.sensors_temperatures()
    doc={"value":temp["acpitz"][0][1]}
    doc["date"]= time_ns()
    doc["sensor_id"]="laptop_temperature_1"


    # tp2
    # client = MongoClient()
    # client = MongoClient('localhost', 27017)
    # db = client.iot
    # collection=db.temp_sensor
    # collection.insert_one(doc).inserted_id
    # collection.find_one()
    # list(collection.find().sort("date",ASCENDING))
    #
    # list(collection.find({"sensor_id":"laptop_temperature"}).sort("date",ASCENDING))
    #
    #collection.remove({})
    credentials = pika.PlainCredentials('rabitmq', 'rabitmq')

    res = json.dumps(doc,default=json_util.default)
    print(res)
    channel.basic_publish(exchange='',
                          routing_key='laptop_temperature',
                          body=res)
    sleep(10)
