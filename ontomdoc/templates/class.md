# [{{onto.label}}](../homepage.md) > {{classe.label}}

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart TB

{%- for triple in triples %}
    {{classe.label}} -- {{triple.predicate}} --> {{triple.id}}[{{triple.range}}]
    class {{triple.id}} literal;
{%- endfor%}
    class {{classe.label}} baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,padding: 0px;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```
