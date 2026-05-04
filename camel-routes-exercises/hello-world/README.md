# Running Hello World

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/hello-world:/app cefriel/chimera:kg4di
```

## JBang Command

```bash
cd camel-routes-exercises/hello-world
jbang camel@apache/camel run camel-routes/*.yaml
```

