# Knowledge Graphs for Data Interoperability (KG4DI)

> Tutorial materials for **"Knowledge Graphs for Data Interoperability with Chimera (KG4DI)"** — a half-day tutorial introducing participants to [Chimera](https://github.com/cefriel/chimera), an open-source framework for building declarative, composable semantic data transformation pipelines on top of Apache Camel.

📄 **Tutorial website:** [https://cefriel.github.io/kg4di](https://cefriel.github.io/kg4di)

---

## Overview

Participants design and execute a complete data integration pipeline — from ingestion of structured data to RDF lifting, SPARQL-based enrichment, SPARQL construction, and RDF lowering — using only YAML route definitions and declarative mapping templates. **No application code is required.**

The running example integrates public transport stop data ([GTFS](https://gtfs.org/) format) with geographic and descriptive information from **Wikidata**, visualised on an interactive map.

---

## Prerequisites

### Required

- **Docker** — used to run all exercises without any local JDK or Python installation.
  - Pull the Chimera image before starting: `docker pull cefriel/chimera:kg4di`
  - Pull the dashboard image: `docker pull cefriel/chimera:kg4di-dashboard`

### Alternative (local execution)

- [JBang](https://www.jbang.dev/) — allows running Chimera pipelines directly on your machine.
  - Install Apache Camel via JBang (first time only):
    ```bash
    jbang app install camel@apache/camel
    ```

---

## Repository Structure

```
camel-routes-exercises/
  hello-world/   # Introductory exercise: Apache Camel basics
  e0/            # Exercise 0: RDF Lifting (CSV → RDF)
  e1/            # Exercise 1: RDF Lowering (RDF → CSV)
  e2/            # Exercise 2: Full pipeline (GTFS → RDF → Wikidata enrichment → visualization)  
visualization/   # Interactive map dashboard
```
---

## Exercises

### [Hello World](camel-routes-exercises/hello-world/README.md)

A minimal Apache Camel route — use this to verify your setup is working correctly before attempting the main exercises.

### [Exercise 0 — RDF Lifting](camel-routes-exercises/e0/README.md)

Lift a CSV file (`stops.txt`) into an RDF knowledge graph by completing an MTL lifting template.

### [Exercise 1 — RDF Lowering](camel-routes-exercises/e1/README.md)

Lower an RDF knowledge graph back into a CSV representation by completing an MTL lowering template.

### [Exercise 2 — Full Pipeline](camel-routes-exercises/e2/README.md)

Build a complete end-to-end pipeline: ingest GTFS data, lift it to RDF, enrich via Wikidata SPARQL CONSTRUCT, and send the result to a visualization backend.

---

## Visualization

The `visualization/` folder contains an interactive map dashboard that displays the results of the pipeline. It can be started alongside Exercise 2 using the included `docker-compose.yaml` at the repository root:

```bash
docker compose up
```

The dashboard will be available at [http://localhost:8000](http://localhost:8000).

---

## Acknowledgements

This work has been partially funded by the European Union's Horizon Europe programme under grant agreements No. 101140087 ([SMARTY](https://www.smarty-project.eu/)), No. 101092908 ([SmartEdge](https://www.smart-edge.eu/)), and No. 101239472 ([UrbanFlow](https://urban-flow.eu/)).
