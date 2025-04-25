# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > based_near

## based near

> **A location that something is based near, for some broadly human notion of near.**

Range :[http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing](<http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing>)
Domain :[http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing](<http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing>)

## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:based_near a rdf:Property,
        owl:ObjectProperty ;
    rdfs:label "based near" ;
    rdfs:comment "A location that something is based near, for some broadly human notion of near." ;
    rdfs:domain <http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing> ;
    rdfs:isDefinedBy foaf: ;
    rdfs:range <http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing> ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*