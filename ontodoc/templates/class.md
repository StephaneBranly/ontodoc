# [{{onto.label}}](../homepage.md) > {{classe.id}}

## {{classe.label if classe.label}}

**{{classe.comment if classe.comment}}**

{% if classe.triples|length %}
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| {%- for triple in classe.triples | sort(attribute='predicate') %} |
| {{triple.predicate}} | {{triple.label if triple.label}} | {{triple.comment if triple.comment}} |

{%- if triple.link -%}
[{{triple.range}}]({{triple.link}}.md)
{%- else -%}
<kbd>{{triple.range}}</kbd>
{%- endif %} |

{%- endfor%}

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
flowchart LR

{%- for triple in classe.triples|sort(attribute='predicate') %}
    {{classe.id}} -- {{triple.predicate}} --> {{triple.id}}[{{triple.range}}]
    class {{triple.id}} literal;
{%- endfor%}
    class {{classe.id}} baseclass;
classDef literal fill:#fcba03,stroke:#333,stroke-width:4px,color:black;
classDef baseclass fill:#030ffc,stroke:#333,stroke-width:4px;
```

{% endif %}
