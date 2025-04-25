# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Group

## Group

> **A class of Agents.**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:member | "member" | "Indicates a member of a Group" |[foaf:Agent](Agent.md) |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Group -- foaf:member --> 0[foaf:Agent]
    class 0 literal;
    class Group baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:Group a rdfs:Class,
        owl:Class ;
    rdfs:label "Group" ;
    rdfs:comment "A class of Agents." ;
    rdfs:subClassOf foaf:Agent ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*