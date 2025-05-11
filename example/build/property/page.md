# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > page

## page

> **A page or document about this thing.**

- Range :[http://xmlns.com/foaf/0.1/Document](../class/Document.md)

- Domain :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Thing --> Document : page
```

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:page a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "page" ;
    rdfs:comment "A page or document about this thing." ;
    rdfs:domain owl:Thing ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Document ;
    owl:inverseOf foaf:topic ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-11

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.2*