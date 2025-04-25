# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Person

## Person

> **A person.**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:currentProject | "current project" | "A current project this person works on." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:family_name | "family_name" | "The family name of some person." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:familyName | "familyName" | "The family name of some person." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:firstName | "firstName" | "The first name of a person." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:geekcode | "geekcode" | "A textual geekcode for this person, see http://www.geekcode.com/geek.html" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:img | "image" | "An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)." |[foaf:Image](Image.md) | |
| foaf:knows | "knows" | "A person known by this person (indicating some level of reciprocated interaction between the parties)." |[foaf:Person](Person.md) | |
| foaf:lastName | "lastName" | "The last name of a person." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:myersBriggs | "myersBriggs" | "A Myers Briggs (MBTI) personality classification." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:pastProject | "past project" | "A project this person has previously worked on." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:plan | "plan" | "A .plan comment, in the tradition of finger and '.plan' files." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:publications | "publications" | "A link to the publications of this person." |[foaf:Document](Document.md) | |
| foaf:schoolHomepage | "schoolHomepage" | "A homepage of a school attended by the person." |[foaf:Document](Document.md) | |
| foaf:surname | "Surname" | "The surname of some person." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:workInfoHomepage | "work info homepage" | "A work info homepage of some person; a page about their work for some organization." |[foaf:Document](Document.md) | |
| foaf:workplaceHomepage | "workplace homepage" | "A workplace homepage of some person; the homepage of an organization they work for." |[foaf:Document](Document.md) |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Person -- foaf:currentProject --> 14[owl:Thing]
    class 14 literal;
    Person -- foaf:family_name --> 4[rdfs:Literal]
    class 4 literal;
    Person -- foaf:familyName --> 5[rdfs:Literal]
    class 5 literal;
    Person -- foaf:firstName --> 1[rdfs:Literal]
    class 1 literal;
    Person -- foaf:geekcode --> 0[rdfs:Literal]
    class 0 literal;
    Person -- foaf:img --> 8[foaf:Image]
    class 8 literal;
    Person -- foaf:knows --> 12[foaf:Person]
    class 12 literal;
    Person -- foaf:lastName --> 2[rdfs:Literal]
    class 2 literal;
    Person -- foaf:myersBriggs --> 7[rdfs:Literal]
    class 7 literal;
    Person -- foaf:pastProject --> 15[owl:Thing]
    class 15 literal;
    Person -- foaf:plan --> 6[rdfs:Literal]
    class 6 literal;
    Person -- foaf:publications --> 13[foaf:Document]
    class 13 literal;
    Person -- foaf:schoolHomepage --> 11[foaf:Document]
    class 11 literal;
    Person -- foaf:surname --> 3[rdfs:Literal]
    class 3 literal;
    Person -- foaf:workInfoHomepage --> 10[foaf:Document]
    class 10 literal;
    Person -- foaf:workplaceHomepage --> 9[foaf:Document]
    class 9 literal;
    class Person baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:Person a rdfs:Class,
        owl:Class ;
    rdfs:label "Person" ;
    rdfs:comment "A person." ;
    rdfs:isDefinedBy foaf: ;
    rdfs:subClassOf <http://www.w3.org/2003/01/geo/wgs84_pos#SpatialThing>,
        foaf:Agent ;
    owl:disjointWith foaf:Organization,
        foaf:Project ;
    owl:equivalentClass <http://schema.org/Person>,
        <http://www.w3.org/2000/10/swap/pim/contact#Person> ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*