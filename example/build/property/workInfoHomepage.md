# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > workInfoHomepage

## work info homepage

> **A work info homepage of some person; a page about their work for some organization.**

Range :[http://xmlns.com/foaf/0.1/Document](Document.md)
Domain :[http://xmlns.com/foaf/0.1/Person](Person.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:workInfoHomepage a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "work info homepage" ;
    rdfs:comment "A work info homepage of some person; a page about their work for some organization." ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Document ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*