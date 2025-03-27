# [{{onto.label}}](../homepage.md) > {{classe.id}}

## {{classe.label if classe.label}}

**{{classe.comment if classe.comment}}**

| Predicate                 | Label                            | Comment                              | Type                                   |
| ------------------------- | -------------------------------- | ------------------------------------ | -------------------------------------- |
| {%- for triple in triples | sort(attribute='predicate') %}   |
| {{triple.predicate}}      | {{triple.label if triple.label}} | {{triple.comment if triple.comment}} | [{{triple.range}}]({{triple.link}}.md) |

{%- endfor%}

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR

{%- for triple in triples|sort(attribute='predicate') %}
    {{classe.id}} -- {{triple.predicate}} --> {{triple.id}}[{{triple.range}}]
    class {{triple.id}} literal;
{%- endfor%}
    class {{classe.id}} baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```
