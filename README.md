### Bike Mobility Analytics

This project demonstrates a real-time bike mobility analytics pipeline using live bike hire data from London.

The pipeline ingests XML data, converts it into Avro format to reduce payload size and enforce schema consistency, and streams the data into Apache Kafka. The data is then processed using ksqlDB for real-time transformations and analytics, and finally visualized through an interactive Streamlit dashboard.

This project showcases a modern event-driven streaming architecture.


#### Architecture Diagram

<img width="1601" height="381" alt="biket drawio" src="https://github.com/user-attachments/assets/a1bc52d5-a3a1-4809-b741-5445c1d8f160" />


#### Technology Stack


Before running the project , ensure you have the following installed:

|  Tool | Version  | Purpose  |
|---|---|---|
|  Java |  17+ |  Runtime for Kafka |
|  Python | 3.9+  | Running script   |
|  Kafka | 4.0.0+  | Distributed Event Streaming   |
|  Schema Registry |  Latest |  Schema Management |
|  Streamlit | Latest  | Dashboard  |
|  KsqlDB | Latest  | Stream Processing   |
|  httpie | Latest  | API Testing   |
|  Uv | Latest  | Python Package Management   |



#### Setup Guide


##### Start Required Services

Ensure the following services are running:

- Kafka broker

- Schema Registry

- ksqlDB server

##### Consume Avro Messages from Kafka

Use the Avro console consumer to inspect messages in the Kafka topic:

```sh
kafka-avro-console-consumer \
  --bootstrap-server localhost:9097 \
  --topic bike.hire \
  --from-beginning \
  --property schema.registry.url=http://localhost:8081

```

This command reads messages from the bike.hire topic and automatically decodes them using the registered Avro schema.


##### Schema Registry

The Schema Registry manages the Avro schema used by producers and consumers.

List all registered subjects:

```sh
http :8081/subjects

```

Check schema versions for the topic:
```sh
http :8081/subjects/bike.hire-value/versions

```

##### Query Data Using ksqlDB REST API

ksqlDB provides a REST API that allows queries to be executed programmatically.

Example query using curl:

```sh
curl -X POST http://localhost:8088/query \
     -H "Content-Type: application/json" \
     -d '{
           "ksql": "SELECT ID, NAME, BIKES, EMPTY_DOCKS, TOTAL_DOCKS FROM BIKE_HIRE_LATEST EMIT CHANGES LIMIT 5;",
           "streamsProperties": {}
         }'
```
