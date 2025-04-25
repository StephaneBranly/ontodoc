# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Organization

## Organization

> **An organization.**



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:Organization a rdfs:Class,
        owl:Class ;
    rdfs:label "Organization" ;
    rdfs:comment "An organization." ;
    rdfs:isDefinedBy foaf: ;
    rdfs:subClassOf foaf:Agent ;
    owl:disjointWith foaf:Document,
        foaf:Person ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*