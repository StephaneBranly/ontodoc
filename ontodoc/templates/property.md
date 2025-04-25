# [{{onto.label}}](../homepage.md) > {{property.id}}

## {{property.label}}

> **{{property.comment}}**

Range : {%- if property.range_link -%}
[{{property.range}}]({{property.range_link}})
{%- elif property.range -%}
<kbd>{{property.range}}</kbd>
{%- endif %}
Domain : {%- if property.domain_link -%}
[{{property.domain}}]({{property.domain_link}})
{%- elif property.domain -%}
<kbd>{{property.domain}}</kbd>
{%- endif %}

## Serialized

```ttl
{{property.serialized}}
```
