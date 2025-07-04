# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > OnlineAccount
<a name="OnlineAccount"></a>
## Online Account

> **An online account.**


## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    class OnlineAccount
    OnlineAccount <|-- OnlineGamingAccount
    OnlineAccount <|-- OnlineEcommerceAccount
    OnlineAccount <|-- OnlineChatAccount
```

## Properties

### Class properties
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
|<kbd>[foaf:accountName](../property/accountName.md)</kbd> | account name | Indicates the name (identifier) associated with this online account. |<kbd>[rdfs:Literal](../<http://www.w3.org/2000/01/rdf-schema#Literal>)</kbd> | |
|<kbd>[foaf:accountServiceHomepage](../property/accountServiceHomepage.md)</kbd> | account service homepage | Indicates a homepage of the service provide for this online account. |<kbd>[foaf:Document](../class/Document.md)</kbd> |



## Serialized

```ttl
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ns1: <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

foaf:OnlineAccount a rdfs:Class,
        owl:Class ;
    rdfs:label "Online Account" ;
    rdfs:comment "An online account." ;
    rdfs:isDefinedBy foaf: ;
    rdfs:subClassOf owl:Thing ;
    ns1:term_status "testing" .


```

---

Documentation generated on 2025-06-25

Generated with <kbd>[📑 ontodoc](https://github.com/StephaneBranly/ontodoc)</kbd>, *v0.0.4*