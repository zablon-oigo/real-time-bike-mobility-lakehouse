from confluent_kafka import SerializingProducer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import StringSerializer
import xml.etree.ElementTree as ET
import httpx
import logging


SCHEMA_REG_URL = "http://localhost:8081"
TOPIC = "bike.hire"
BASE_URL = "https://tfl.gov.uk/tfl/syndication/feeds/cycle-hire/livecyclehireupdates.xml"

# Load Avro schema
with open("schema.avro", "r") as f:
    schema_str = f.read()


# Create Schema Registry client
sr_client = SchemaRegistryClient({"url": SCHEMA_REG_URL})

def dict_to_avro(obj, ctx):
    return obj

