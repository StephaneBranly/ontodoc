# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Agent

## Agent

> **An agent (eg. person, group, software or physical artifact).**

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    class Agent
    Agent <|-- Organization
    Agent <|-- Group
    Agent <|-- Person
```


## Properties
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
|[foaf:account](../property/account.md) | "account" | "Indicates an account held by this agent." |[foaf:OnlineAccount](../class/OnlineAccount.md) | |
|[foaf:age](../property/age.md) | "age" | "The age in years of some agent." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:age](../property/age.md) | "age" | "The age in years of some agent." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:aimChatID](../property/aimChatID.md) | "AIM chat ID" | "An AIM chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:birthday](../property/birthday.md) | "birthday" | "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:birthday](../property/birthday.md) | "birthday" | "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:gender](../property/gender.md) | "gender" | "The gender of this Agent (typically but not necessarily 'male' or 'female')." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:gender](../property/gender.md) | "gender" | "The gender of this Agent (typically but not necessarily 'male' or 'female')." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:holdsAccount](../property/holdsAccount.md) | "account" | "Indicates an account held by this agent." |[foaf:OnlineAccount](../class/OnlineAccount.md) | |
|[foaf:icqChatID](../property/icqChatID.md) | "ICQ chat ID" | "An ICQ chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:interest](../property/interest.md) | "interest" | "A page about a topic of interest to this person." |[foaf:Document](../class/Document.md) | |
|[foaf:jabberID](../property/jabberID.md) | "jabber ID" | "A jabber ID for something." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:made](../property/made.md) | "made" | "Something that was made by this agent." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
|[foaf:mbox](../property/mbox.md) | "personal mailbox" | "A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
|[foaf:mbox_sha1sum](../property/mbox_sha1sum.md) | "sha1sum of a personal mailbox URI name" | "The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:msnChatID](../property/msnChatID.md) | "MSN chat ID" | "An MSN chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:openid](../property/openid.md) | "openid" | "An OpenID for an Agent." |[foaf:Document](../class/Document.md) | |
|[foaf:skypeID](../property/skypeID.md) | "Skype ID" | "A Skype ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:status](../property/status.md) | "status" | "A string expressing what the user is happy for the general public (normally) to know about their current activity." |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) | |
|[foaf:tipjar](../property/tipjar.md) | "tipjar" | "A tipjar document for this agent, describing means for payment and reward." |[foaf:Document](../class/Document.md) | |
|[foaf:topic_interest](../property/topic_interest.md) | "topic_interest" | "A thing of interest to this person." |[owl:Thing](<http://www.w3.org/2002/07/owl#Thing>) | |
|[foaf:weblog](../property/weblog.md) | "weblog" | "A weblog of some thing (whether person, group, company etc.)." |[foaf:Document](../class/Document.md) | |
|[foaf:yahooChatID](../property/yahooChatID.md) | "Yahoo chat ID" | "A Yahoo chat ID" |[rdfs:Literal](<http://www.w3.org/2000/01/rdf-schema#Literal>) |


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

Documentation generated on 2025-05-02

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.1*