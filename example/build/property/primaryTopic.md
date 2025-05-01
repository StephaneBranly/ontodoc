# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > primaryTopic

## primary topic

> **The primary topic of some page or document.**

- Range :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

- Domain :[http://xmlns.com/foaf/0.1/Document](../class/Document.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Document -> Thing : primary topic
```


## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:primaryTopic a rdf:Property,
        owl:FunctionalProperty,
        owl:ObjectProperty ;
    rdfs:label "primary topic" ;
    rdfs:comment "The primary topic of some page or document." ;
    rdfs:domain foaf:Document ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range owl:Thing ;
    owl:inverseOf foaf:isPrimaryTopicOf ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*