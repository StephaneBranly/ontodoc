# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > nick

## nickname

> **A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames).**

Range :
Domain :

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:nick a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "nickname" ;
    rdfs:comment "A short informal nickname characterising an agent (includes login identifiers, IRC and other chat nicknames)." ;
    rdfs:isDefinedBy foaf: ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*