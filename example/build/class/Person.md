# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Person

## Person

**A person.**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:currentProject | "current project" | "A current project this person works on." |<kbd>owl:Thing</kbd> | |
| foaf:family_name | "family_name" | "The family name of some person." |<kbd>rdfs:Literal</kbd> | |
| foaf:familyName | "familyName" | "The family name of some person." |<kbd>rdfs:Literal</kbd> | |
| foaf:firstName | "firstName" | "The first name of a person." |<kbd>rdfs:Literal</kbd> | |
| foaf:geekcode | "geekcode" | "A textual geekcode for this person, see http://www.geekcode.com/geek.html" |<kbd>rdfs:Literal</kbd> | |
| foaf:img | "image" | "An image that can be used to represent some thing (ie. those depictions which are particularly representative of something, eg. one's photo on a homepage)." |<kbd>foaf:Image</kbd> | |
| foaf:knows | "knows" | "A person known by this person (indicating some level of reciprocated interaction between the parties)." |<kbd>foaf:Person</kbd> | |
| foaf:lastName | "lastName" | "The last name of a person." |<kbd>rdfs:Literal</kbd> | |
| foaf:myersBriggs | "myersBriggs" | "A Myers Briggs (MBTI) personality classification." |<kbd>rdfs:Literal</kbd> | |
| foaf:pastProject | "past project" | "A project this person has previously worked on." |<kbd>owl:Thing</kbd> | |
| foaf:plan | "plan" | "A .plan comment, in the tradition of finger and '.plan' files." |<kbd>rdfs:Literal</kbd> | |
| foaf:publications | "publications" | "A link to the publications of this person." |<kbd>foaf:Document</kbd> | |
| foaf:schoolHomepage | "schoolHomepage" | "A homepage of a school attended by the person." |<kbd>foaf:Document</kbd> | |
| foaf:surname | "Surname" | "The surname of some person." |<kbd>rdfs:Literal</kbd> | |
| foaf:workInfoHomepage | "work info homepage" | "A work info homepage of some person; a page about their work for some organization." |<kbd>foaf:Document</kbd> | |
| foaf:workplaceHomepage | "workplace homepage" | "A workplace homepage of some person; the homepage of an organization they work for." |<kbd>foaf:Document</kbd> |

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
    Person -- foaf:img --> 7[foaf:Image]
    class 7 literal;
    Person -- foaf:knows --> 12[foaf:Person]
    class 12 literal;
    Person -- foaf:lastName --> 2[rdfs:Literal]
    class 2 literal;
    Person -- foaf:myersBriggs --> 8[rdfs:Literal]
    class 8 literal;
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



---

Documentation generated on 2025-04-16

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*