### Bike Mobility

```sh
kafka-avro-console-consumer \
  --bootstrap-server localhost:9097 \
  --topic bike.hire \
  --from-beginning \
  --property schema.registry.url=http://localhost:8081

```


```sh
http :8081/subjects
http :8081/subjects/bike.hire-value/versions

```

Test Query Via HTTP POST
```sh
curl -X POST http://localhost:8088/query \
     -H "Content-Type: application/json" \
     -d '{
           "ksql": "SELECT ID, NAME, BIKES, EMPTY_DOCKS, TOTAL_DOCKS FROM BIKE_HIRE_LATEST EMIT CHANGES LIMIT 5;",
           "streamsProperties": {}
         }'
```