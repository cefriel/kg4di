# Running Exercise 0

We want to lift the CSV lower [./inbox/stops.txt](./inbox/stops.txt) to obtain the the RDF KG contained in [./outbox/e0-output.ttl](./outbox/e0-output.ttl).

To do this, edit and complete the MTL mapping in [./lifting.vm](./lifting.vm).

Use the commands below to run the mappings and check the output obtained through the logs or in [./outbox/e0-exercise-output.ttl].

## Using Docker Compose

```bash
cd camel-routes-exercises/e0
docker compose up
```

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/e0:/app cefriel/chimera:kg4di
# container must be explicitly killed with command [docker kill <container_id_or_name>]
```

## JBang Command

```bash
cd camel-routes-exercises/e0
jbang camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0
```

