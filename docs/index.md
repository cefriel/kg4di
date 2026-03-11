---
layout: default
title: "Knowledge Graphs for Data Interoperability with Chimera (KG4DI)"
permalink: /
---

## Semantic Data Integration with Chimera

This half-day tutorial introduces participants to **Chimera**, an open-source framework for building declarative, composable semantic data transformation pipelines on top of Apache Camel. The tutorial addresses the practical challenges of achieving data interoperability across heterogeneous sources using knowledge graphs as a unifying model.

The session combines a conceptual introduction with a guided hands-on exercise. Participants will design and execute a complete data integration pipeline — from ingestion of structured data to RDF lifting, SPARQL-based enrichment and construction, and RDF lowering — using only YAML route definitions and declarative mapping templates. No application code is required.

A mobility scenario (integration of public transport data with open knowledge from Wikidata) is used throughout as a running example to ground the concepts in a concrete, realistic setting.

---

## Learning Outcomes

By the end of this tutorial, participants will be able to:

- Explain the **any-to-RDF-to-any** integration pattern and its role in enabling semantic interoperability
- Configure **Apache Camel routes** augmented with Chimera components for data transformation tasks
- Write **lifting and lowering templates** using the Mapping Template Language (MTL) to convert between arbitrary formats and RDF
- Apply **SPARQL CONSTRUCT** queries within a pipeline to build and reshape knowledge graphs
- Integrate external **SPARQL endpoints** (e.g. Wikidata) as enrichment sources in a declarative pipeline
- Deploy and run a complete end-to-end pipeline using the provided Docker environment

---

## Running Example

To illustrate the pipeline stages, participants will work with a scenario involving the integration of public transport stop data (in **GTFS** format) with geographic and descriptive information retrieved from **Wikidata**. The resulting knowledge graph is visualised on an interactive map that updates as data flows through the pipeline.

![Interactive map showing public transport stops enriched with Wikidata landmarks](./dubrovnik.png)

*An interactive dashboard fed by the Chimera pipeline that will be built during the hands-on session.*

This scenario is representative of a broad class of integration problems encountered in domains such as smart cities, industry 4.0, and health data management, where heterogeneous sources can be unified under a common semantic model.

---

## Tutorial Structure

| Segment | Duration | Content |
|---------|----------|---------|
| **Part 1 — Data Interoperability Challenges** | 45 min | Key challenges in heterogeneous data integration; limitations of ad-hoc approaches; knowledge graphs as a unifying model |
| **Part 2 — The Chimera Framework** | 45 min | Architecture overview; the any-to-RDF-to-any pattern; Chimera component library; Mapping Template Language (MTL) |
| **Break** | 15 min | |
| **Part 3 — Hands-on Session** | 1 h 30 min | Guided pipeline construction: ingestion, lifting, SPARQL enrichment, construction, lowering, and visualisation |

---

## Pipeline Stages Covered

Participants will configure and run each of the following stages during the hands-on session:

| Stage | Description |
|-------|-------------|
| **Ingest** | Read structured data files (CSV within ZIP archives) using Apache Camel routes |
| **Lift** | Convert tabular records to RDF triples using MTL lifting templates |
| **Enrich** | Query a remote SPARQL endpoint (Wikidata) to retrieve additional structured information |
| **Construct** | Shape the knowledge graph using SPARQL `CONSTRUCT` queries |
| **Lower** | Serialise RDF back to a target format (CSV) using MTL lowering templates |
| **Visualise** | Observe pipeline output in a live interactive map interface |

---

## Prerequisites

Participants are expected to have:

- A laptop with **Docker** installed (all software dependencies are provided as container images; no local JDK or Python installation is required)
- Basic familiarity with structured data formats (CSV, JSON)
- Basic knowledge of **RDF** and the Semantic Web stack (recommended)

---

## Tutorial Materials

Slides and all required materials will be made available on this page before the start of the conference.

- **Slides:** _To be published_
- **Docker image & setup instructions:** _To be published_
- **Chimera repository:** <https://github.com/cefriel/chimera>
- **Chimera tutorial repository:** <https://github.com/cefriel/chimera-tutorial>

---

## Presenters

### Marco Grassi
*Knowledge Technologies Researcher, Cefriel*
Marco Grassi's research focuses on semantic technologies and data interoperability. He is the lead developer of the Chimera framework and the principal author of its tutorial materials.

### Mario Scrocca
*Senior Knowledge Technologies Researcher, Cefriel*
Mario Scrocca's research interests include knowledge representation, data management, and semantic interoperability, with applications in mobility and industrial domains. He is a maintainer of the Chimera framework and has co-organised tutorials on Knowledge Graph Construction at ESWC 2022 and ESWC 2024.

### Alessio Carenini
*Senior Researcher and Software Architect, Cefriel*
Alessio Carenini has over 18 years of experience in European research projects, with a focus on the application of Semantic Web technologies to knowledge management in data-sharing ecosystems, including metadata modelling and data spaces.

### Irene Celino
*Research Line Manager, Cefriel*
Irene Celino coordinates research activities at Cefriel. Her interests span knowledge graphs, semantic interoperability, human-in-the-loop AI, and the human-centric evaluation of AI systems, with over 20 years of experience in cooperative research projects.

---

## References

**Grassi, M., Scrocca, M., Carenini, A., Comerio, M., Celino, I.**
Composable semantic data transformation pipelines with Chimera.
In: *Proceedings of the 4th International Workshop on Knowledge Graph Construction*, co-located with ESWC 2023.
CEUR Workshop Proceedings, vol. 3471. CEUR (May 2023).
[PDF](https://ceur-ws.org/Vol-3471/paper9.pdf) — ISSN 1613-0073

**Scrocca, M., Carenini, A., Grassi, M., Comerio, M., Celino, I.**
Not everybody speaks RDF: Knowledge conversion between different data representations.
In: *Proceedings of the 5th International Workshop on Knowledge Graph Construction*, co-located with ESWC 2024.
CEUR Workshop Proceedings, vol. 3718. CEUR (May 2024).
[PDF](https://ceur-ws.org/Vol-3718/paper3.pdf) — ISSN 1613-0073

**Scrocca, M., Comerio, M., Carenini, A., Celino, I.**
Turning transport data to comply with EU standards while enabling a multimodal transport knowledge graph.
In: *Proceedings of the 19th International Semantic Web Conference (ISWC 2020)*.
Lecture Notes in Computer Science, vol. 12507, pp. 411–429. Springer (2020).
[DOI](https://doi.org/10.1007/978-3-030-62466-8_26)

---


<div class="ack-banner">
<img src="https://www.smarty-project.eu/wp-content/uploads/2024/04/SMARTY-Electric-blue-only-logo-no-BG-COMPLETE.png" alt="SMARTY logo" style="height:32px;vertical-align:middle;margin-right:10px;">
This work has been partially funded by the European Union's Horizon Europe research and innovation programme under grant agreement No. 101140087 (<a href="https://www.smarty-project.eu/" target="_blank" rel="noopener noreferrer">SMARTY</a>, Chips Joint Undertaking).
</div>

