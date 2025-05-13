# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > sha1

## sha1sum (hex)

> **A sha1sum hash, in hex.**



- Domain :[http://xmlns.com/foaf/0.1/Document](../class/Document.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:sha1 a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "sha1sum (hex)" ;
    rdfs:comment "A sha1sum hash, in hex." ;
    rdfs:domain foaf:Document ;
    rdfs:isDefinedBy foaf: ;
    ns1:term_status "unstable" .


```

---

Documentation generated on 2025-05-13

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.3*