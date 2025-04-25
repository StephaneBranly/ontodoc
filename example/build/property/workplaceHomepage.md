# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > workplaceHomepage

## workplace homepage

> **A workplace homepage of some person; the homepage of an organization they work for.**

Range :[http://xmlns.com/foaf/0.1/Document](Document.md)
Domain :[http://xmlns.com/foaf/0.1/Person](Person.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:workplaceHomepage a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "workplace homepage" ;
    rdfs:comment "A workplace homepage of some person; the homepage of an organization they work for." ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range foaf:Document ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*