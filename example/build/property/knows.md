# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > knows

## knows

> **A person known by this person (indicating some level of reciprocated interaction between the parties).**

Range :[http://xmlns.com/foaf/0.1/Person](Person.md)
Domain :[http://xmlns.com/foaf/0.1/Person](Person.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:knows a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "knows" ;
    rdfs:comment "A person known by this person (indicating some level of reciprocated interaction between the parties)." ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Person ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*