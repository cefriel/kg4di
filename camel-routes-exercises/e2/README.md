# Running Exercise 2

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/e2:/app cefriel/chimera:kg4di
```


## JBang Command

```bash
cd camel-routes-exercises/e2
jbang camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0
```

