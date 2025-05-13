# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > currentProject

## current project

> **A current project this person works on.**

- Range :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

- Domain :[http://xmlns.com/foaf/0.1/Person](../class/Person.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Person --> Thing : current project
```

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:currentProject a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "current project" ;
    rdfs:comment "A current project this person works on." ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range owl:Thing ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-13

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.3*