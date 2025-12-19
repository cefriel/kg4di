---
layout: default
title: "Knowledge Graphs for Data Interoperability with Chimera (KG4DI)"
permalink: /
---

## Abstract

Achieving data interoperability across heterogeneous information
systems is a critical challenge in many real-world
scenarios. Knowledge graphs offer a powerful foundation for addressing
this need, yet implementing such solutions is complex due to diverse
data models, evolving requirements, and the prevalence of ad-hoc
integrations. In this tutorial, we first examine the key challenges
and typical requirements for enabling interoperability, illustrated
through practical scenarios. We then introduce an approach based on
any-to-one mappings to knowledge graphs, supported by a modular
toolbox that enables scalable and low-code integration. Specifically,
we present the Chimera framework, which provides reusable and
configurable components for defining transformation
pipelines. Participants will gain hands-on experience by applying this
approach to a concrete scenario, configuring and executing Chimera
pipelines to achieve interoperability in practice.

---

## Tutorial Outline

This half-day tutorial will follow the indicative schedule outlined hereafter:
1. Challenges of Data Interoperability (45 min)
2. Enable Data Interoperability through Semantic Data Pipelines (45 min)
3. Break
4. Hands-on Session (1h 30min)

The hands-on session centres on building an interactive mobility
dashboard that integrates heterogeneous datasets to generate insights
for transportation and tourism stakeholders. Participants will be
guided to develop several data pipelines to retrieve, harmonize, and
exchange multiple data sources.

Through these data pipelines, participants will feed data into a
dashboard application that displays the locations of train and bus
stations and enriches them with contextual information such as nearby
landmarks and current weather conditions. They will work directly with
data sourced from GTFS (General Transit Feed Specification) files for
static public transport data, Wikidata queries for points of interest,
and a weather API for real-time meteorological information.
Participants will follow an end-to-end workflow to retrieve and
harmonize these diverse datasets using the Chimera framework. They
will build data pipelines to access raw data, transform and harmonise
it into RDF based on a conceptual model using declarative mapping
languages, and ensure semantic consistency and interoperability across
sources. Finally, participants will convert the RDF output into the
data formats supported by the dashboard (GeoJSON, JSON) and visualise
the results within the interactive dashboard.

---

## Speakers

### Marco Grassi  
*Knowledge Technologies Researcher, Cefriel*  
Marco Grassi focuses on semantic technologies and data interoperability. He is the lead developer of the Chimera framework and the main author of the Chimera tutorial available on GitHub.

### Mario Scrocca  
*Senior Knowledge Technologies Researcher, Cefriel*  
Mario Scrocca’s research focuses on knowledge representation, data management, and interoperability, with applications in the mobility and industrial domains. He is one of the maintainers of the Chimera framework and has co-organized tutorials on Knowledge Graph Construction, including at ESWC 2022.

### Alessio Carenini  
*Senior Researcher, Technical Leader, and Senior Software Architect, Cefriel*  
Alessio Carenini has over 18 years of experience in European research projects. His work focuses on applying Semantic Web technologies to knowledge management in data sharing ecosystems, with interests in metadata modeling, data spaces, and business process management.

### Irene Celino  
*Research Line Manager, Cefriel*  
Irene Celino coordinates research activities at Cefriel and has over 20 years of experience in cooperative research projects. Her interests include Knowledge Graphs, semantic interoperability, human-in-the-loop and hybrid AI, and human-centric evaluation of AI.

---

## References and Further Reading

**Chimera repository**: <https://github.com/cefriel/chimera>  

**Chimera tutorial repository**: <https://github.com/cefriel/chimera-tutorial>  

**Grassi, M., Scrocca, M., Carenini, A., Comerio, M., Celino, I.**  
Composable semantic data transformation pipelines with Chimera.  
In: *Proceedings of the 4th International Workshop on Knowledge Graph Construction*  
co-located with the 20th Extended Semantic Web Conference.  
CEUR Workshop Proceedings, vol. 3471. CEUR, Hersonissos, Greece (May 2023).  
[PDF](https://ceur-ws.org/Vol-3471/paper9.pdf)  
ISSN: 1613-0073

**Scrocca, M., Carenini, A., Grassi, M., Comerio, M., Celino, I.**  
Not everybody speaks RDF: Knowledge conversion between different data representations.  
In: *Proceedings of the 5th International Workshop on Knowledge Graph Construction*.  
CEUR Workshop Proceedings, vol. 3718. CEUR, Hersonissos, Greece (May 2024).  
[PDF](https://ceur-ws.org/Vol-3718/paper3.pdf)  
ISSN: 1613-0073

**Scrocca, M., Comerio, M., Carenini, A., Celino, I.**  
Turning transport data to comply with EU standards while enabling a multimodal transport knowledge graph.  
In: *Proceedings of the 19th International Semantic Web Conference*.  
Lecture Notes in Computer Science, vol. 12507, pp. 411–429. Springer (2020).  
[DOI](https://doi.org/10.1007/978-3-030-62466-8_26)


---

## Slides and Tutorial Materials

Slides and tutorial materials will be made available on this page as
soon as they are ready, and no later than the start of the conference.

- **Slides:** _To be published_  
- **Necessary Software and dependencies:** _To be published_  

Please check back closer to the conference date for updates.
