# {{onto.label}}

{{onto.comment}}

{% if onto.contributor and onto.contributor|length %} ## Contributors
{% for contributor in onto.contributor%}

- {{contributor}}{%- endfor %}
  {% endif %}

## Summary

- **{{onto.classes|length}}** classes
- **{{onto.objectProperties|length + onto.datatypeProperties|length + onto.annotationProperties|length + onto.functionalProperties|length}}** Properties
  - **{{onto.objectProperties|length}}** object
  - **{{onto.datatypeProperties|length}}** datatype
  - **{{onto.annotationProperties|length}}** annotation
  - **{{onto.functionalProperties|length}}** functional

## Classes

{% for class in onto.classes %}
[{{class.label}}](class/{{class.id}}.md),
{%- endfor %}

## Properties

### Object Properties

{% for property in onto.objectProperties %}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor %}

### Datatype Properties

{% for property in onto.datatypeProperties %}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor %}

### Annotation Properties

{% for property in onto.annotationProperties %}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor %}

### Functional Properties

{% for property in onto.functionalProperties %}
[{{property.label}}](property/{{property.id}}.md),
{%- endfor %}

## Namepaces

{% for namespace in onto.namespaces%}

- <kbd>{{namespace.prefix}}:</kbd> {{namespace.uri}},
  {%- endfor %}
