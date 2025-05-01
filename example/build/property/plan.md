# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > plan

## plan

> **A .plan comment, in the tradition of finger and '.plan' files.**

- Range :[http://www.w3.org/2000/01/rdf-schema#Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)

- Domain :[http://xmlns.com/foaf/0.1/Person](../class/Person.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Person -> Literal : plan
```


## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:plan a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "plan" ;
    rdfs:comment "A .plan comment, in the tradition of finger and '.plan' files." ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*