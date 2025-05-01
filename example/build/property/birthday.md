# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > birthday

## birthday

> **The birthday of this Agent, represented in mm-dd string form, eg. '12-31'.**

- Range :[http://www.w3.org/2000/01/rdf-schema#Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)

- Domain :[http://xmlns.com/foaf/0.1/Agent](../class/Agent.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:birthday a rdf:Property,
        owl:DatatypeProperty,
        owl:FunctionalProperty ;
    rdfs:label "birthday" ;
    rdfs:comment "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." ;
    rdfs:domain foaf:Agent ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "unstable" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*