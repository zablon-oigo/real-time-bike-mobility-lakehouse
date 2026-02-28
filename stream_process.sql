-- Create Source Stream from Kafka topic

CREATE STREAM BIKE_HIRE_SRC (
    id          VARCHAR KEY,
    name        VARCHAR,
    bikes       INT,
    empty_docks INT,
    total_docks INT
) WITH (
    KAFKA_TOPIC='bike.hire',
    VALUE_FORMAT='AVRO'
);