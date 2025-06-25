# [{{onto.label}}]({{class.to_root_path}}{{onto.pagename}}) > {{class.id}}
<a name="{{class.id}}"></a>
## {{class.label if class.label}}

{% if class.comment -%}> **{{class.comment}}**{% endif %}
{% if class.deprecated %}
> [!CAUTION]
> Deprecated class
{%- endif %}

{%- if metadata.with_schema %}

## Schema

```mermaid
---
config:
  look: neo
  theme: neo
---
classDiagram
    class {{class.id}}
    
    {%- if class.subclassof %}
    {%- for subclassof in class.subclassof %}
    {{subclassof.id}} <|-- {{class.id}}
    {%- endfor -%}
    {% endif %}
    
    {%- if class.subclasses %}
    {%- for subclass in class.subclasses %}
    {{class.id}} <|-- {{subclass.id}}
    {%- endfor -%}
    {% endif %}
```
{%- endif %}

## Properties
{% if class.triples|length %}
### Class properties
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| {%- for triple in class.triples | sort(attribute='n3') %} |
| {%- if triple.pagename -%}
<kbd>[{{triple.n3}}]({{class.to_root_path}}{{triple.pagename}})</kbd>
{%- else -%}
<kbd>{{triple.n3}}</kbd>
{%- endif %} | {{triple.label if triple.label}} | {{triple.comment if triple.comment}} |

{%- if triple.range_link -%}
<kbd>[{{triple.range_n3}}]({{class.to_root_path}}{{triple.range_link}})</kbd>
{%- else -%}
<kbd>{{triple.range_n3}}</kbd>
{%- endif %} |
{%- endfor%}
{% endif %}

{%- if class.subclassof %}
{%- for subclassof in class.subclassof %}
  {% if subclassof.triples|length %}
### Inherited from <kbd>[**{{subclassof.label}}**](../{{subclassof.pagename}}.md)</kbd>
| Predicate | Label | Comment | Type |
| -------------------------------- | -------------------------------- | ------------------------------------ | ---- |
| {%- for triple in subclassof.triples | sort(attribute='n3') %} |
| {%- if triple.pagename -%}
<kbd>[{{triple.n3}}]({{class.to_root_path}}{{triple.pagename}})</kbd>
{%- else -%}
<kbd>{{triple.n3}}</kbd>
{%- endif %} | {{triple.label if triple.label}} | {{triple.comment if triple.comment}} |

{%- if triple.range_link -%}
<kbd>[{{triple.range_n3}}]({{class.to_root_path}}{{triple.range_link}})</kbd>
{%- else -%}
<kbd>{{triple.range_n3}}</kbd>
{%- endif %} |
{%- endfor%}
{% endif %}
{%- endfor -%}
{% endif %}


## Serialized

```ttl
{{class.serialized}}
```
