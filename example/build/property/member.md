# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > member

## member

> **Indicates a member of a Group**

- Range :[http://xmlns.com/foaf/0.1/Agent](../class/Agent.md)

- Domain :[http://xmlns.com/foaf/0.1/Group](../class/Group.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Group -> Agent : member
```


## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:member a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "member" ;
    rdfs:comment "Indicates a member of a Group" ;
    rdfs:domain foaf:Group ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Agent ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*