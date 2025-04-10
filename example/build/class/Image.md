# [Friend of a Friend (FOAF) vocabulary](../homepage.md) > Image

## Image

**An image.**

| Predicate                        | Label                            | Comment                              | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
|   |
| foaf:depicts             | "depicts" | "A thing depicted in this representation." |<kbd>owl:Thing</kbd> |   |
| foaf:thumbnail             | "thumbnail" | "A derived thumbnail image." |<kbd>foaf:Image</kbd> |

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR
    Image -- foaf:depicts --> 0[owl:Thing]
    class 0 literal;
    Image -- foaf:thumbnail --> 1[foaf:Image]
    class 1 literal;
    class Image baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```

---

Documentation generated on 2025-04-10

Generated with [📑 ontodoc](https://github.com/StephaneBranly/ontodoc), *v0.0.0*