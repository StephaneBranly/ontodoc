# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > givenname
<a name="givenname"></a>
## Given name

> **The given name of some person.**






## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:givenname a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "Given name" ;
    rdfs:comment "The given name of some person." ;
    rdfs:isDefinedBy foaf: ;
    ns1:term_status "archaic" .


```

---

Documentation generated on 2025-06-25

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.4*