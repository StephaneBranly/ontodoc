# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > geekcode
<a name="geekcode"></a>
## geekcode

> **A textual geekcode for this person, see http://www.geekcode.com/geek.html**


- Range :[http://www.w3.org/2000/01/rdf-schema#Literal](../<http://www.w3.org/2000/01/rdf-schema#Literal>)

- Domain :[http://xmlns.com/foaf/0.1/Person](../class/Person.md)

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    Person --> Literal : geekcode
```

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:geekcode a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "geekcode" ;
    rdfs:comment "A textual geekcode for this person, see http://www.geekcode.com/geek.html" ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "archaic" .


```

---

Documentation generated on 2025-06-25

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.4*