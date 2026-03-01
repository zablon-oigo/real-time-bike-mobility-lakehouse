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


-- Quick query 
SET 'auto.offset.reset' = 'earliest';

SELECT 
    TIMESTAMPTOSTRING(ROWTIME,'yyyy-MM-dd HH:mm:ss','Europe/London') AS LASTUPDATE,
    ID,
    NAME,
    BIKES,
    EMPTY_DOCKS,
    TOTAL_DOCKS
FROM BIKE_HIRE_SRC
EMIT CHANGES
LIMIT 5;


-- Stream for downstream processing

CREATE STREAM BIKE_HIRE_CLEANED AS
SELECT
    ID,
    NAME,
    BIKES,
    EMPTY_DOCKS,
    TOTAL_DOCKS
FROM BIKE_HIRE_SRC
EMIT CHANGES;


-- Quick Query 

SELECT * 
FROM BIKE_HIRE_CLEANED
EMIT CHANGES
LIMIT 5;

