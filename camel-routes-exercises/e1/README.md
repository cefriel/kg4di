# Exercise 1 - Lowering

We want to lower the RDF KG contained in [./inbox/e1-input.ttl](./inbox/e1-input.ttl) to the CSV representation in file [./outbox/e1-output.csv](./outbox/e1-output.csv).

To do this, edit and complete the MTL mapping in [./lowering.vm](./lowering.vm).

# How to run the mapping

## Using Docker Compose

```bash
cd camel-routes-exercises/e1
docker compose up
```

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/e1:/app cefriel/chimera:kg4di
```

## JBang Command

```bash
cd camel-routes-exercises/e1
jbang camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0
```

