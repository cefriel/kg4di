# Running Hello World

## Using Docker Compose

```bash
cd camel-routes-exercises/hello-world
docker compose up
docker compose down
```

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/hello-world:/app cefriel/chimera:kg4di
# container must be explicitly killed with command [docker kill <container_id_or_name>]
```

## JBang Command

```bash
cd camel-routes-exercises/hello-world
jbang camel@apache/camel run camel-routes/*.yaml
```

