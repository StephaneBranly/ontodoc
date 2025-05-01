# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > accountServiceHomepage

## account service homepage

> **Indicates a homepage of the service provide for this online account.**

- Range :[http://xmlns.com/foaf/0.1/Document](../class/Document.md)

- Domain :[http://xmlns.com/foaf/0.1/OnlineAccount](../class/OnlineAccount.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    OnlineAccount --> Document : account service homepage
```


## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:accountServiceHomepage a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "account service homepage" ;
    rdfs:comment "Indicates a homepage of the service provide for this online account." ;
    rdfs:domain foaf:OnlineAccount ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Document ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*