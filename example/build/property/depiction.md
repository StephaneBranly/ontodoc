# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > depiction

## depiction

> **A depiction of some thing.**

Range :[http://xmlns.com/foaf/0.1/Image](Image.md)
Domain :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:depiction a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "depiction" ;
    rdfs:comment "A depiction of some thing." ;
    rdfs:domain owl:Thing ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Image ;
    owl:inverseOf foaf:depicts ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*