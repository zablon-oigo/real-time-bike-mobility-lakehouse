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

# Create Avro serializer
avro_serializer = AvroSerializer(
    schema_registry_client=sr_client,
    schema_str=schema_str,
    to_dict=dict_to_avro
)

# Create Serializing Producer
producer = SerializingProducer({
    "bootstrap.servers": "localhost:9097,localhost:9095,localhost:9102",
    "key.serializer": StringSerializer("utf_8"),
    "value.serializer": avro_serializer
})


def fetch_live_bike_hire():
    try:
        response = httpx.get(BASE_URL, timeout=10.0)
        response.raise_for_status()

        root = ET.fromstring(response.text)
        stations = []
        for station in root.findall(".//station"):
            stations.append({
                "id": station.findtext("id"),
                "name": station.findtext("name"),
                "bikes": int(station.findtext("nbBikes")),
                "empty_docks": int(station.findtext("nbEmptyDocks")),
                "total_docks": int(station.findtext("nbDocks")),
            })

