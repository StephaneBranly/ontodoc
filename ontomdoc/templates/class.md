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
{%- endfor%}
```
