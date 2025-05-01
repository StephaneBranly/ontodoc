# [{{onto.label}}](../homepage.md) > {{classe.id}}

## {{classe.label if classe.label}}

> **{{classe.comment if classe.comment}}**

{% if classe.triples|length %}
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
