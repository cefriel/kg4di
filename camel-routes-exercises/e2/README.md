# Exercise 2

This exercise is divided into three sequential stages:

# 1. Lifting GTFS Data (`lifting.yaml` route)

### Overview

This route:

* Reads GTFS input data from the `e2/inbox` folder
* Lifts the data into a semantic representation
* Enriches it with Wikidata information via a construct process
* Passes the enriched output to the lowering stage

### Tasks

1. **Input placement**

   * Place your GTFS feed inside:

     ```
     e2/inbox
     ```

2. **Define Chimera resource**

   * Create a `ChimeraResourceBean` that references the mapping file:

     ```
     e2/mappings/lifting.vm
     ```

3. **Perform the lifting step**

   * Use the Camel Chimera Mapping Template component:
     [https://cefriel.github.io/chimera/mapt-component/](https://cefriel.github.io/chimera/mapt-component/)

---

# 2. Enrichment via Wikidata (SPARQL CONSTRUCT)

### Overview

After lifting, the system generates a CONSTRUCT query that must be executed against Wikidata.

### Task

* Execute the generated **CONSTRUCT query** using the appropriate Chimera Graph Component operation:
  [https://cefriel.github.io/chimera/graph-component/](https://cefriel.github.io/chimera/graph-component/)

### Result

* The lifted GTFS data is enriched with Wikidata information and prepared for lowering.

---

# 3. Lowering and Visualization (`lowering.yaml` route)

### Overview

This final route:

* Lowers the enriched semantic data back into a target format
* Sends it to a visualization backend via HTTP

### Task

* Use the **Apache Camel HTTP component** to send the lowered data via HTTP POST to:

```
https://knowledge.c-innovationhub.com/kg4di/api/location
```

Documentation:
[https://camel.apache.org/components/4.18.x/http-component.html](https://camel.apache.org/components/4.18.x/http-component.html)

### Result

* The processed data is transmitted to the visualization system for display.

### Running Exercise 2

## Using Docker Compose

```bash
cd camel-routes-exercises/e2
docker compose up
docker compose down
```

## Docker Command

```bash
# from root directory
docker run -v ./camel-routes-exercises/e2:/app cefriel/chimera:kg4di
# container must be explicitly killed with command [docker kill <container_id_or_name>]
```


## JBang Command

```bash
cd camel-routes-exercises/e2
jbang --java-options="-Dhttp.agent=MyCustomAgent/1.0" camel@apache/camel run camel-routes/*.yaml --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0 ../functions/GeoFunctions.java
```

### Local Deployment

If you want to experiment with the exercise after the tutorial, you can use the complete docker-compose file to execute also the web app. In the pipeline, you have to set the HTTP request to `http://dashboard:8000/api/location`.

```bash
cd camel-routes-exercises/e2
docker compose -f docker-compose-with-dashboard.yaml up
docker compose -f docker-compose-with-dashboard.yaml down
```