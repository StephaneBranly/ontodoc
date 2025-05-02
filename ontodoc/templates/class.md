# [{{onto.label}}](../homepage.md) > {{classe.id}}

## {{classe.label if classe.label}}

> **{{classe.comment if classe.comment}}**

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    class {{classe.label}}
    
    {%- if classe.subclassof %}
    {%- for subclassof in classe.subclassof %}
    {{subclassof}} <|-- {{classe.label}}
    {%- endfor -%}
    {% endif %}
    
    {%- if classe.subclasses %}
    {%- for subclass in classe.subclasses %}
    {{classe.label}} <|-- {{subclass}}
    {%- endfor -%}
    {% endif %}
```

{% if classe.triples|length %}
## Properties
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| {%- for triple in classe.triples | sort(attribute='predicate') %} |
| {%- if triple.predicate_link -%}
[{{triple.predicate}}]({{triple.predicate_link}})
{%- else -%}
<kbd>{{triple.range}}</kbd>
{%- endif %} | {{triple.label if triple.label}} | {{triple.comment if triple.comment}} |

{%- if triple.range_link -%}
[{{triple.range}}]({{triple.range_link}})
{%- else -%}
<kbd>{{triple.range}}</kbd>
{%- endif %} |
{%- endfor%}
{% endif %}

## Serialized

```ttl
{{classe.serialized}}
```
