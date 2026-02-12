import json
import os
from dotenv import load_dotenv
load_dotenv()
from confluent_kafka import Consumer
from mysql_connection import connection
from init_db import insert_customers ,insert_orders

consumer_config = {
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker",
    "auto.offset.reset": "earliest"
}

consumer = Consumer(consumer_config)

consumer.subscribe(["orders"])

print("🟢 Consumer is running and subscribed to orders topic")


try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            print("❌ Error:", msg.error())
            continue

        value = msg.value().decode('utf-8')
        item = json.loads(value)
        if item ["type"] == "customer":
            insert_customers(connection,item)

        elif item ["type"] == "order":
            insert_orders(connection,item)

        print(f"📦 Received order: {item }")
except KeyboardInterrupt:
    print("\n🔴 Stopping consumer")

finally:
    consumer.close()


