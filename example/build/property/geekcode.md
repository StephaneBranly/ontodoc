# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > geekcode

## geekcode

> **A textual geekcode for this person, see http://www.geekcode.com/geek.html**

Range :[http://www.w3.org/2000/01/rdf-schema#Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>)
Domain :[http://xmlns.com/foaf/0.1/Person](Person.md)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:geekcode a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "geekcode" ;
    rdfs:comment "A textual geekcode for this person, see http://www.geekcode.com/geek.html" ;
    rdfs:domain foaf:Person ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "archaic" .


```

---

Documentation generated on 2025-05-01

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*