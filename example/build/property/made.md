# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > made

## made

> **Something that was made by this agent.**

- Range :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

- Domain :[http://xmlns.com/foaf/0.1/Agent](../class/Agent.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Agent --> Thing : made
```


## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:made a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "made" ;
    rdfs:comment "Something that was made by this agent." ;
    rdfs:domain foaf:Agent ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range owl:Thing ;
    owl:inverseOf foaf:maker ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*