# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > OnlineAccount

## Online Account

**An online account.**

| Predicate                        | Label                            | Comment                              | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
|   |
| foaf:accountName             | "account name" | "Indicates the name (identifier) associated with this online account." |<kbd>rdfs:Literal</kbd> |   |
| foaf:accountServiceHomepage             | "account service homepage" | "Indicates a homepage of the service provide for this online account." |<kbd>foaf:Document</kbd> |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    OnlineAccount -- foaf:accountName --> 1[rdfs:Literal]
    class 1 literal;
    OnlineAccount -- foaf:accountServiceHomepage --> 0[foaf:Document]
    class 0 literal;
    class OnlineAccount baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef literal fill:#1cba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
classDef baseclass fill:#130ffc,stroke:#333,stroke-width:4px;
```

---

Documentation generated on 2025-04-13

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*