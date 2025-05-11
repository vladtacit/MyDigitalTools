# consumer_j.py
# Simple consumer for probes (json)

from kafka import KafkaConsumer
import json

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('mix-events',
                         group_id='group-J',
                         bootstrap_servers=['localhost:9092'])

# consume json messages
KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))

for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
