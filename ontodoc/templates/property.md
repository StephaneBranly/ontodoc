# [{{onto.label}}]({{property.to_root_path}}{{onto.pagename}}) > {{property.id}}
<a name="{{property.id}}"></a>
## {{property.label}}

{% if property.comment -%}> **{{property.comment}}**{% endif %}
{% if property.deprecated %}
> [!CAUTION]
> Deprecated property
{%- endif %}

{% if property.range -%}
- Range : {%- if property.range_link -%}
[{{property.range}}]({{property.to_root_path}}{{property.range_link}})
{%- elif property.range%}
<kbd>{{property.range}}</kbd>
{%- endif %}{%- endif %}

{% if property.domain -%}
- Domain : {%- if property.domain_link -%}
[{{property.domain}}]({{property.to_root_path}}{{property.domain_link}})
{%- elif property.domain -%}
<kbd>{{property.domain}}</kbd>
{%- endif %}{%- endif %}
{%- if metadata.with_schema %}
{%- if property.domain and property.range %}

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    {{property.domain_label}} --> {{property.range_label}} : {{property.label}}
```
{%- endif %}
{%- endif %}

## Serialized

```ttl
{{property.serialized}}
```
