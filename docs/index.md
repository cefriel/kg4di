---
layout: default
title: "Knowledge Graphs for Data Interoperability with Chimera (KG4DI)"
permalink: /
---

## Overview

This half-day tutorial introduces participants to the practical challenges of achieving data interoperability across heterogeneous sources and to the advantages of an approach based on knowledge graphs [[1](https://arxiv.org/pdf/2011.06423)]. Considering a practical scenario in the mobility domain (the integration of public transport data with open knowledge from Wikidata), participants will learn how knowledge graphs can support data harmonisation and fusion.

The session combines a conceptual introduction with a guided hands-on exercise using **Chimera** [[2](https://ceur-ws.org/Vol-3471/paper9.pdf)], an [open-source framework](https://github.com/cefriel/chimera) for building declarative and composable semantic data transformation pipelines. Participants will design and execute a complete data integration pipeline — from ingestion of structured data to RDF lifting, SPARQL-based enrichment and construction, and RDF lowering — using only YAML route definitions and declarative mapping templates [[3](https://ceur-ws.org/Vol-3718/paper3.pdf)]. No programming experience is required.

---

## Learning Outcomes

By the end of this tutorial, participants will be able to:

- Explain the **any-to-RDF-to-any** integration pattern and its role in enabling semantic interoperability
- Configure **[Apache Camel](https://camel.apache.org/) routes** augmented with [Chimera](https://github.com/cefriel/chimera) components for data transformation tasks
- Write **lifting and lowering templates** using the [Mapping Template Language (MTL)](https://github.com/cefriel/mapping-template/wiki/Mapping-Template-Language-(MTL)) to convert between arbitrary formats and RDF
- Apply **semantic transformations** within a pipeline to build and reshape knowledge graphs
- Integrate external **data sources** (e.g. Wikidata SPARQL endpoint) as enrichment sources in a declarative pipeline
- **Deploy and run** a complete end-to-end pipeline using the provided Docker environment

---

## Running Example

To illustrate the pipeline stages, participants will work with a scenario involving the integration of public transport stop data (in [**GTFS**](https://gtfs.org/) format) with geographic and descriptive information retrieved from [**Wikidata**](https://www.wikidata.org/wiki/Wikidata:Main_Page). The resulting knowledge graph is visualised on an interactive online map that updates as data flows through the pipelines built by the participants.

![Interactive map showing public transport stops enriched with Wikidata landmarks](./assets/media/dubrovnik.png)

*An interactive dashboard fed by the Chimera pipeline that will be built during the hands-on session.*

This scenario is representative of a broad class of integration problems encountered in domains such as smart cities, industry 4.0, and health data management, where heterogeneous sources can be unified under a common semantic model [[4](https://arxiv.org/pdf/2407.10539),[5](https://arxiv.org/pdf/2508.02708)].

---

## Tutorial Structure

| Segment | Duration | Content |
|---------|----------|---------|
| **Introduction** | 15 min | Motivation, objectives and practical information |
| **Part 1 — Data Interoperability Challenges** | 20 min + [5 min] | Key challenges in heterogeneous data integration; limitations of ad-hoc approaches; knowledge graphs as a unifying model + [presentation of the tutorial use case] |
| **Part 2 — Mapping Approaches** | 20 min + [30 min] | State of the art; the any-to-RDF-to-any pattern; [RDF Mapping Language (RML)](https://w3id.org/rml/portal) vs [Mapping Template Language (MTL)](https://github.com/cefriel/mapping-template/wiki/Mapping-Template-Language-(MTL)) + [exercises for lifting/lowering mapping rules] |
| **Break** | 30 min | |
| **Part 3 — Chimera Framework** | 30 min + [1 hour] | [Chimera](https://github.com/cefriel/chimera) concepts and related components; Chimera in action + [guided pipeline construction for the tutorial use case: ingestion, lifting, SPARQL enrichment, construction, lowering, and visualisation] |

---

## Pipeline Stages Covered

Participants will configure and run each of the following stages during the hands-on session:

| Stage | Description |
|-------|-------------|
| **Ingest** | Read structured data files (CSV within ZIP archives) re-using the wide library of [Apache Camel](https://camel.apache.org/) components within [Chimera](https://github.com/cefriel/chimera) pipelines |
| **Lift** | Convert tabular records to RDF triples using [MTL](https://github.com/cefriel/mapping-template/wiki/Mapping-Template-Language-(MTL)) lifting templates |
| **Enrich** | Query a remote SPARQL endpoint (Wikidata) to retrieve additional structured information |
| **Construct** | Shape the knowledge graph using SPARQL `CONSTRUCT` queries |
| **Lower** | Serialise RDF back to a target format (CSV) using [MTL](https://github.com/cefriel/mapping-template/wiki/Mapping-Template-Language-(MTL)) lowering templates |
| **Visualise** | Observe pipeline output in a live interactive map interface |

---

## Prerequisites

Participants are expected to have:

- A laptop with **Docker** installed (all software dependencies are provided as container images; no local JDK or Python installation is required): [How to install Docker](https://docs.docker.com/engine/install/)
- Basic familiarity with structured data formats (CSV, JSON)
- Basic knowledge of **RDF** and the Semantic Web stack (recommended)

---

## Tutorial Materials

Slides and all required materials will be made available on this page before the start of the conference.

- **Slides:** _To be published_
- **Docker image & setup instructions:** _To be published_
- **Chimera repository:** <https://github.com/cefriel/chimera>

---

## Presenters

<div class="presenter-bio">
  <img src="./assets/media/grassi.jpg" alt="Marco Grassi" class="presenter-image">
  <div>
    <h3>Marco Grassi</h3>
    <p><b>Instructor</b> <em>Knowledge Technologies Researcher, Cefriel</em></p>
    <p>Marco Grassi's research focuses on semantic technologies and data interoperability. He is the lead developer of the Chimera framework and the principal author of its tutorial materials.</p>
  </div>
</div>

<div class="presenter-bio">
  <img src="./assets/media/scrocca.jpg" alt="Mario Scrocca" class="presenter-image">
  <div>
    <h3>Mario Scrocca</h3>
    <p><b>Instructor</b> <em>Senior Knowledge Technologies Researcher, Cefriel</em></p>
    <p>Mario Scrocca's research interests include knowledge representation, data management, and semantic interoperability, with applications in mobility and industrial domains. He is a maintainer of the Chimera framework and has co-organised tutorials and courses on Knowledge Graph Construction topics.</p>
  </div>
</div>

<div class="presenter-bio">
  <img src="./assets/media/carenini.jpg" alt="Alessio Carenini" class="presenter-image">
  <div>
    <h3>Alessio Carenini</h3>
    <p><b>Organizer</b> <em>Senior Researcher and Software Architect, Cefriel</em></p>
    <p>Alessio Carenini has over 18 years of experience in European research projects, with a focus on the application of Semantic Web technologies to knowledge management in data-sharing ecosystems, including metadata modelling and data spaces.</p>
  </div>
</div>

<div class="presenter-bio">
  <img src="./assets/media/celino.jpg" alt="Irene Celino" class="presenter-image">
  <div>
    <h3>Irene Celino</h3>
    <p><b>Organizer</b> <em>Research Line Manager, Cefriel</em></p>
    <p>Irene Celino coordinates research activities at Cefriel. Her interests span knowledge graphs, semantic interoperability, human-in-the-loop AI, and the human-centric evaluation of AI systems, with over 20 years of experience in cooperative research projects.</p>
  </div>
</div>

---

## References

[1] **Scrocca, M., Comerio, M., Carenini, A., Celino, I.**
[Turning transport data to comply with EU standards while enabling a multimodal transport knowledge graph](https://arxiv.org/pdf/2011.06423).
In: *Proceedings of the 19th International Semantic Web Conference (ISWC 2020)*.
Lecture Notes in Computer Science, vol. 12507, pp. 411–429. Springer (2020).
[DOI](https://doi.org/10.1007/978-3-030-62466-8_26), [arXiv](https://arxiv.org/pdf/2011.06423)

[2] **Grassi, M., Scrocca, M., Carenini, A., Comerio, M., Celino, I.**
[Composable semantic data transformation pipelines with Chimera](https://ceur-ws.org/Vol-3471/paper9.pdf).
In: *Proceedings of the 4th International Workshop on Knowledge Graph Construction*, co-located with ESWC 2023.
CEUR Workshop Proceedings, vol. 3471. CEUR (May 2023).
[CEUR](https://ceur-ws.org/Vol-3471/paper9.pdf)

[3] **Scrocca, M., Carenini, A., Grassi, M., Comerio, M., Celino, I.**
[Not everybody speaks RDF: Knowledge conversion between different data representations](https://ceur-ws.org/Vol-3718/paper3.pdf).
In: *Proceedings of the 5th International Workshop on Knowledge Graph Construction*, co-located with ESWC 2024.
CEUR Workshop Proceedings, vol. 3718. CEUR (May 2024).
[CEUR](https://ceur-ws.org/Vol-3718/paper3.pdf)

[4] **Scrocca, M., et al.**
[Intelligent Urban Traffic Management via Semantic Interoperability Across Multiple Heterogeneous Mobility Data Sources](https://arxiv.org/pdf/2407.10539).
In: *Proceedings of the 23rd International Semantic Web Conference (ISWC 2024)*.
Springer Nature Switzerland, Cham (November 2024).
[DOI](https://doi.org/10.1007/978-3-031-77847-6_12), [arXiv](https://arxiv.org/pdf/2407.10539)

[5] **Scrocca, M., Grassi, M., Carenini, A., Anicic, D., Calbimonte, J. P., & Celino, I.**
[A DataOps Toolbox Enabling Continuous Semantic Integration of Devices for Edge‑Cloud AI Applications](https://arxiv.org/pdf/2508.02708).
In: *Proceedings of the 24th International Semantic Web Conference (ISWC 2025)*.
Springer Nature Switzerland, Cham (October 2025).
[DOI](https://doi.org/10.1007/978-3-032-09530-5_22), [arXiv](https://arxiv.org/pdf/2508.02708)

---


<div class="ack-banner">
<img src="https://www.smarty-project.eu/wp-content/uploads/2024/04/SMARTY-Electric-blue-only-logo-no-BG-COMPLETE.png" alt="SMARTY logo" style="height:32px;vertical-align:middle;margin-right:10px;">
This work has been partially funded by the European Union's Horizon Europe research and innovation programme under grant agreement No. 101140087 (<a href="https://www.smarty-project.eu/" target="_blank" rel="noopener noreferrer">SMARTY</a>, Chips Joint Undertaking).
</div>
<div class="ack-banner">
<img src="https://www.smart-edge.eu/wp-content/uploads/2024/03/logo-smartedge-full.png" alt="SmartEdge logo" style="height:32px;vertical-align:middle;margin-right:10px;">
This work has been partially funded by the European Union's Horizon Europe research and innovation programme under grant agreement No. 101092908 (<a href="https://www.smart-edge.eu/" target="_blank" rel="noopener noreferrer">SmartEdge</a>).
</div>
<div class="ack-banner">
<img src="./assets/media/urban_flow_project_logo.jpg" alt="UrbanFlow logo" style="height:32px;vertical-align:middle;margin-right:10px;">
This work has been partially funded by the European Union's Horizon Europe research and innovation programme under grant agreement No. 101239472 (<a href="https://urban-flow.eu/" target="_blank" rel="noopener noreferrer">UrbanFlow</a>).
</div>

