# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > msnChatID
<a name="msnChatID"></a>
## MSN chat ID

> **An MSN chat ID**


- Range :[http://www.w3.org/2000/01/rdf-schema#Literal](../<http://www.w3.org/2000/01/rdf-schema#Literal>)

- Domain :[http://xmlns.com/foaf/0.1/Agent](../class/Agent.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Agent --> Literal : MSN chat ID
```

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:msnChatID a rdf:Property,
        owl:DatatypeProperty,
        owl:InverseFunctionalProperty ;
    rdfs:label "MSN chat ID" ;
    rdfs:comment "An MSN chat ID" ;
    rdfs:domain foaf:Agent ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    rdfs:subPropertyOf foaf:nick ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-06-25

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.4*