# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Document

## Document

**A document.**

| Predicate                        | Label                            | Comment                              | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
|   |
| foaf:primaryTopic             | "primary topic" | "The primary topic of some page or document." |<kbd>owl:Thing</kbd> |   |
| foaf:topic             | "topic" | "A topic of some page or document." |<kbd>owl:Thing</kbd> |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Document -- foaf:primaryTopic --> 1[owl:Thing]
    class 1 literal;
    Document -- foaf:topic --> 0[owl:Thing]
    class 0 literal;
    class Document baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef literal fill:#1cba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
classDef baseclass fill:#130ffc,stroke:#333,stroke-width:4px;
```

---

Documentation generated on 2025-04-13

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*