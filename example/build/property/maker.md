# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > maker

## maker

> **An agent that  made this thing.**

- Range :[http://xmlns.com/foaf/0.1/Agent](../class/Agent.md)

- Domain :[http://www.w3.org/2002/07/owl#Thing](<http://www.w3.org/2002/07/owl#Thing>)

## Serialized

```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:maker a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "maker" ;
    rdfs:comment "An agent that  made this thing." ;
    rdfs:domain owl:Thing ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Agent ;
    owl:equivalentProperty dcterms:creator ;
    owl:inverseOf foaf:made ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*