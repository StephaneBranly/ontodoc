# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Agent

## Agent

**An agent (eg. person, group, software or physical artifact).**


| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| |
| foaf:account | "account" | "Indicates an account held by this agent." |<kbd>foaf:OnlineAccount</kbd> | |
| foaf:age | "age" | "The age in years of some agent." |<kbd>rdfs:Literal</kbd> | |
| foaf:aimChatID | "AIM chat ID" | "An AIM chat ID" |<kbd>rdfs:Literal</kbd> | |
| foaf:birthday | "birthday" | "The birthday of this Agent, represented in mm-dd string form, eg. '12-31'." |<kbd>rdfs:Literal</kbd> | |
| foaf:gender | "gender" | "The gender of this Agent (typically but not necessarily 'male' or 'female')." |<kbd>rdfs:Literal</kbd> | |
| foaf:holdsAccount | "account" | "Indicates an account held by this agent." |<kbd>foaf:OnlineAccount</kbd> | |
| foaf:icqChatID | "ICQ chat ID" | "An ICQ chat ID" |<kbd>rdfs:Literal</kbd> | |
| foaf:interest | "interest" | "A page about a topic of interest to this person." |<kbd>foaf:Document</kbd> | |
| foaf:jabberID | "jabber ID" | "A jabber ID for something." |<kbd>rdfs:Literal</kbd> | |
| foaf:made | "made" | "Something that was made by this agent." |<kbd>owl:Thing</kbd> | |
| foaf:mbox | "personal mailbox" | "A  personal mailbox, ie. an Internet mailbox associated with exactly one owner, the first owner of this mailbox. This is a 'static inverse functional property', in that  there is (across time and change) at most one individual that ever has any particular value for foaf:mbox." |<kbd>owl:Thing</kbd> | |
| foaf:mbox_sha1sum | "sha1sum of a personal mailbox URI name" | "The sha1sum of the URI of an Internet mailbox associated with exactly one owner, the  first owner of the mailbox." |<kbd>rdfs:Literal</kbd> | |
| foaf:msnChatID | "MSN chat ID" | "An MSN chat ID" |<kbd>rdfs:Literal</kbd> | |
| foaf:openid | "openid" | "An OpenID for an Agent." |<kbd>foaf:Document</kbd> | |
| foaf:skypeID | "Skype ID" | "A Skype ID" |<kbd>rdfs:Literal</kbd> | |
| foaf:status | "status" | "A string expressing what the user is happy for the general public (normally) to know about their current activity." |<kbd>rdfs:Literal</kbd> | |
| foaf:tipjar | "tipjar" | "A tipjar document for this agent, describing means for payment and reward." |<kbd>foaf:Document</kbd> | |
| foaf:topic_interest | "topic_interest" | "A thing of interest to this person." |<kbd>owl:Thing</kbd> | |
| foaf:weblog | "weblog" | "A weblog of some thing (whether person, group, company etc.)." |<kbd>foaf:Document</kbd> | |
| foaf:yahooChatID | "Yahoo chat ID" | "A Yahoo chat ID" |<kbd>rdfs:Literal</kbd> |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Agent -- foaf:account --> 15[foaf:OnlineAccount]
    class 15 literal;
    Agent -- foaf:age --> 18[rdfs:Literal]
    class 18 literal;
    Agent -- foaf:aimChatID --> 4[rdfs:Literal]
    class 4 literal;
    Agent -- foaf:birthday --> 17[rdfs:Literal]
    class 17 literal;
    Agent -- foaf:gender --> 2[rdfs:Literal]
    class 2 literal;
    Agent -- foaf:holdsAccount --> 16[foaf:OnlineAccount]
    class 16 literal;
    Agent -- foaf:icqChatID --> 6[rdfs:Literal]
    class 6 literal;
    Agent -- foaf:interest --> 13[foaf:Document]
    class 13 literal;
    Agent -- foaf:jabberID --> 3[rdfs:Literal]
    class 3 literal;
    Agent -- foaf:made --> 12[owl:Thing]
    class 12 literal;
    Agent -- foaf:mbox --> 0[owl:Thing]
    class 0 literal;
    Agent -- foaf:mbox_sha1sum --> 1[rdfs:Literal]
    class 1 literal;
    Agent -- foaf:msnChatID --> 8[rdfs:Literal]
    class 8 literal;
    Agent -- foaf:openid --> 10[foaf:Document]
    class 10 literal;
    Agent -- foaf:skypeID --> 5[rdfs:Literal]
    class 5 literal;
    Agent -- foaf:status --> 19[rdfs:Literal]
    class 19 literal;
    Agent -- foaf:tipjar --> 11[foaf:Document]
    class 11 literal;
    Agent -- foaf:topic_interest --> 14[owl:Thing]
    class 14 literal;
    Agent -- foaf:weblog --> 9[foaf:Document]
    class 9 literal;
    Agent -- foaf:yahooChatID --> 7[rdfs:Literal]
    class 7 literal;
    class Agent baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```



---

Documentation generated on 2025-04-16

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*