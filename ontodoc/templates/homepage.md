# {{onto.label}}

_{{onto.onto_node}}_

> {{onto.comment}}

{% if onto.creator and onto.creator|length %}
## Creators
{% for creator in onto.creator%}
- {{creator}}{%- endfor %}
{% endif %}

{% if onto.contributor and onto.contributor|length %}
## Contributors
{% for contributor in onto.contributor%}
- {{contributor}}{%- endfor %}
{% endif %}

## Summary

{% if onto.versionInfo %}- Version : **{{onto.versionInfo}}**{% endif %}
{% if onto.created %}- Creation date : **{{onto.created}}**{% endif %}
{% if onto.modified %}- Modification date : **{{onto.modified}}**{% endif %}
- **{{onto.classes|length}}** classes
- **{{onto.objectProperties|length + onto.datatypeProperties|length + onto.annotationProperties|length + onto.functionalProperties|length}}** Properties
  - **{{onto.objectProperties|length}}** object
  - **{{onto.datatypeProperties|length}}** datatype
  - **{{onto.annotationProperties|length}}** annotation
  - **{{onto.functionalProperties|length}}** functional

{% if onto.classes and onto.classes|length -%}
## Classes

{% for class in onto.classes | sort(attribute='label') -%}
[{{class.label}}](class/{{class.id}}.md),
{%- endfor -%}
{%- endif%}

## Properties

{% if onto.objectProperties and onto.objectProperties|length -%}
### Object Properties

{% for property in onto.objectProperties | sort(attribute='label') -%}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor -%}
{%- endif%}

{% if onto.datatypeProperties and onto.datatypeProperties|length -%}
### Datatype Properties

{% for property in onto.datatypeProperties | sort(attribute='label') -%}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor -%}
{%- endif%}

{% if onto.annotationProperties and onto.annotationProperties|length -%}
### Annotation Properties

{% for property in onto.annotationProperties | sort(attribute='label') -%}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor -%}
{%- endif%}

{% if onto.functionalProperties and onto.functionalProperties|length -%}
### Functional Properties

{% for property in onto.functionalProperties | sort(attribute='label') -%}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor -%}
{%- endif %}

## Namepaces

{% for namespace in onto.namespaces | sort(attribute='prefix')%}
- <kbd>{{namespace.prefix}}:</kbd> {{namespace.uri}},
{%- endfor %}

## Download ontology

[Ontology available here](./ontology.ttl)
