from confluent_kafka import Producer
import os
from dotenv import load_dotenv
load_dotenv()
import json
from time import sleep
from mongo_connection import coll


def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
    else:
        print(f"✅ Delivered {msg.value().decode('utf-8')}")
        print(f"✅ Delivered to {msg.topic()} :"
              f" partition {msg.partition()} : at offset {msg.offset()}")


producer_config = {
    "bootstrap.servers": os.getenv("TEST_K_SERVER")
}

producer = Producer(producer_config)


total = len(list(coll.find()))
count_skip = 0
for i in range(0,total,30):
    res = coll.find({},{"_id":0}).limit(30).skip(count_skip)
    for r in res:
        value = json.dumps(r).encode("utf-8")
        producer.produce(
                topic="orders",
                value=value,
                callback=delivery_report)
        producer.flush()
        sleep(0.5)

    count_skip += 30





