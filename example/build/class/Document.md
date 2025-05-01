# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Document

## Document

> **A document.**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:primaryTopic | "primary topic" | "The primary topic of some page or document." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:primaryTopic | "primary topic" | "The primary topic of some page or document." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:sha1 | "sha1sum (hex)" | "A sha1sum hash, in hex." |<kbd>None</kbd> | |
| foaf:topic | "topic" | "A topic of some page or document." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Document -- foaf:primaryTopic --> 1[owl:Thing]
    class 1 literal;
    Document -- foaf:primaryTopic --> 3[owl:Thing]
    class 3 literal;
    Document -- foaf:sha1 --> 0[None]
    class 0 literal;
    Document -- foaf:topic --> 2[owl:Thing]
    class 2 literal;
    class Document baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:Document a rdfs:Class,
        owl:Class ;
    rdfs:label "Document" ;
    rdfs:comment "A document." ;
    rdfs:isDefinedBy foaf: ;
    owl:disjointWith foaf:Organization,
        foaf:Project ;
    owl:equivalentClass <http://schema.org/CreativeWork> ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*