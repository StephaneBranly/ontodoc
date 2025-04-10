# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Group

## Group

**A class of Agents.**

| Predicate                        | Label                            | Comment                              | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
|   |
| foaf:member             | "member" | "Indicates a member of a Group" |<kbd>foaf:Agent</kbd> |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Group -- foaf:member --> 0[foaf:Agent]
    class 0 literal;
    class Group baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```

---

Documentation generated on 2025-04-10

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*