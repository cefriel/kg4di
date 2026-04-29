# Running Exercise 3

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/e3:/app cefriel/chimera:kg4di
```


## JBang Command

```bash
cd camel-routes-exercises/e3
jbang --java-options="-Dhttp.agent=MyCustomAgent/1.0" camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0 GeoFunctions.java
```

