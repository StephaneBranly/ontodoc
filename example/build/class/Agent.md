# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Agent

## Agent

> **An agent (eg. person, group, software or physical artifact).**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:account | "account" | "Indicates an account held by this agent." |[foaf:OnlineAccount](OnlineAccount.md) | |
| foaf:age | "age" | "The age in years of some agent." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:age | "age" | "The age in years of some agent." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:aimChatID | "AIM chat ID" | "An AIM chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:birthday | "birthday" | "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:birthday | "birthday" | "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:gender | "gender" | "The gender of this Agent (typically but not necessarily 'male' or 'female')." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:gender | "gender" | "The gender of this Agent (typically but not necessarily 'male' or 'female')." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:holdsAccount | "account" | "Indicates an account held by this agent." |[foaf:OnlineAccount](OnlineAccount.md) | |
| foaf:icqChatID | "ICQ chat ID" | "An ICQ chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:interest | "interest" | "A page about a topic of interest to this person." |[foaf:Document](Document.md) | |
| foaf:jabberID | "jabber ID" | "A jabber ID for something." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:made | "made" | "Something that was made by this agent." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:mbox | "personal mailbox" | "A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:mbox_sha1sum | "sha1sum of a personal mailbox URI name" | "The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:msnChatID | "MSN chat ID" | "An MSN chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:openid | "openid" | "An OpenID for an Agent." |[foaf:Document](Document.md) | |
| foaf:skypeID | "Skype ID" | "A Skype ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:status | "status" | "A string expressing what the user is happy for the general public (normally) to know about their current activity." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
| foaf:tipjar | "tipjar" | "A tipjar document for this agent, describing means for payment and reward." |[foaf:Document](Document.md) | |
| foaf:topic_interest | "topic_interest" | "A thing of interest to this person." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
| foaf:weblog | "weblog" | "A weblog of some thing (whether person, group, company etc.)." |[foaf:Document](Document.md) | |
| foaf:yahooChatID | "Yahoo chat ID" | "A Yahoo chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Agent -- foaf:account --> 21[foaf:OnlineAccount]
    class 21 literal;
    Agent -- foaf:age --> 9[rdfs:Literal]
    class 9 literal;
    Agent -- foaf:age --> 13[rdfs:Literal]
    class 13 literal;
    Agent -- foaf:aimChatID --> 3[rdfs:Literal]
    class 3 literal;
    Agent -- foaf:birthday --> 8[rdfs:Literal]
    class 8 literal;
    Agent -- foaf:birthday --> 12[rdfs:Literal]
    class 12 literal;
    Agent -- foaf:gender --> 1[rdfs:Literal]
    class 1 literal;
    Agent -- foaf:gender --> 11[rdfs:Literal]
    class 11 literal;
    Agent -- foaf:holdsAccount --> 22[foaf:OnlineAccount]
    class 22 literal;
    Agent -- foaf:icqChatID --> 5[rdfs:Literal]
    class 5 literal;
    Agent -- foaf:interest --> 19[foaf:Document]
    class 19 literal;
    Agent -- foaf:jabberID --> 2[rdfs:Literal]
    class 2 literal;
    Agent -- foaf:made --> 18[owl:Thing]
    class 18 literal;
    Agent -- foaf:mbox --> 14[owl:Thing]
    class 14 literal;
    Agent -- foaf:mbox_sha1sum --> 0[rdfs:Literal]
    class 0 literal;
    Agent -- foaf:msnChatID --> 7[rdfs:Literal]
    class 7 literal;
    Agent -- foaf:openid --> 16[foaf:Document]
    class 16 literal;
    Agent -- foaf:skypeID --> 4[rdfs:Literal]
    class 4 literal;
    Agent -- foaf:status --> 10[rdfs:Literal]
    class 10 literal;
    Agent -- foaf:tipjar --> 17[foaf:Document]
    class 17 literal;
    Agent -- foaf:topic_interest --> 20[owl:Thing]
    class 20 literal;
    Agent -- foaf:weblog --> 15[foaf:Document]
    class 15 literal;
    Agent -- foaf:yahooChatID --> 6[rdfs:Literal]
    class 6 literal;
    class Agent baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```



## Serialized

```ttl
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:Agent a rdfs:Class,
        owl:Class ;
    rdfs:label "Agent" ;
    rdfs:comment "An agent (eg. person, group, software or physical artifact)." ;
    owl:equivalentClass dcterms:Agent ;
    ns1:term_status "stable" .


```

---

Documentation generated on 2025-04-25

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*