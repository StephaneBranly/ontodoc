# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > dnaChecksum
<a name="dnaChecksum"></a>
## DNA checksum

> **A checksum for the DNA of some thing. Joke.**


- Range :[http://www.w3.org/2000/01/rdf-schema#Literal](../<http://www.w3.org/2000/01/rdf-schema#Literal>)



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:dnaChecksum a rdf:Property,
        owl:DatatypeProperty ;
    rdfs:label "DNA checksum" ;
    rdfs:comment "A checksum for the DNA of some thing. Joke." ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range rdfs:Literal ;
    ns1:term_status "archaic" .


```

---

Documentation generated on 2025-06-25

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.4*