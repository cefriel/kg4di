# Knowledge Graphs for Data Interoperability (KG4DI)

> Tutorial materials for **"Knowledge Graphs for Data Interoperability with Chimera (KG4DI)"** — a half-day tutorial introducing participants to [Chimera](https://github.com/cefriel/chimera), an open-source framework for building declarative, composable semantic data transformation pipelines on top of Apache Camel.

📄 **Tutorial website:** [https://cefriel.github.io/kg4di](https://cefriel.github.io/kg4di)

---

## Overview

Participants design and execute a complete data integration pipeline — from ingestion of structured data to RDF lifting, SPARQL-based enrichment, SPARQL construction, and RDF lowering — using only YAML route definitions and declarative mapping templates. **No application code is required.**

The running example integrates public transport stop data (GTFS format) with geographic and descriptive information from **Wikidata**, visualised on an interactive map.

---

## Prerequisites

- **Docker** (recommended) — no local JDK installation required.
- Alternatively, [JBang](https://www.jbang.dev/) for running the pipeline locally.

---

## Running with Docker (Recommended)

```bash
docker compose up
```

---

## Running Locally

Requires [JBang](https://www.jbang.dev/) installed.

**1. Install Apache Camel (first time only):**

```bash
jbang app install camel@apache/camel
```

**2. Run the pipeline from within your routes directory:**

```bash
cd camel-routes-exercises   # or camel-routes-solved
jbang --java-options="-Dhttp.agent=MyCustomAgent/1.0" camel@apache/camel run *.yaml \
  --dep=mvn:com.cefriel:camel-chimera-mapping-template:4.6.0 \
  ../GeoFunctions.java
```

---

## Visualization

The `visualization/` folder contains an interactive map dashboard. It is included in `docker-compose.yaml` and starts automatically with `docker compose up`, served at [http://localhost:8000](http://localhost:8000). To run it standalone:

```bash
docker run -p 8000:8000 cefriel/chimera:kg4di-dashboard
```

---

## Acknowledgements

This work has been partially funded by the European Union's Horizon Europe programme under grant agreements No. 101140087 ([SMARTY](https://www.smarty-project.eu/)), No. 101092908 ([SmartEdge](https://www.smart-edge.eu/)), and No. 101239472 ([UrbanFlow](https://urban-flow.eu/)).
