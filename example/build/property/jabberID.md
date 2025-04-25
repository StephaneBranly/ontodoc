# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > jabberID

## jabber ID

> **A jabber ID for something.**

Range :[http://www.w3.org/2000/01/rdf-schema#Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
Domain :[http://xmlns.com/foaf/0.1/Agent](Agent.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:jabberID a rdf:Property,
        owl:DatatypeProperty,
        owl:InverseFunctionalProperty ;
    rdfs:label "jabber ID" ;
    rdfs:comment "A jabber ID for something." ;
    rdfs:domain foaf:Agent ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*