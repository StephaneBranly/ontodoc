# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > focus

## focus

> **The underlying or 'focal' entity associated with some SKOS-described concept.**

Range :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)
Domain :[http://www.w3.org/2004/02/skos/core#Concept](<http://www.w3.org/2004/02/skos/core#Concept>)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

foaf:focus a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "focus" ;
    rdfs:comment "The underlying or 'focal' entity associated with some SKOS-described concept." ;
    rdfs:domain skos:Concept ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range owl:Thing ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*