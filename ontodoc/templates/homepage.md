# {{onto.label}}

{{onto.comment}}

{% if onto.contributor and onto.contributor|length %} ## Contributors
{% for contributor in onto.contributor%}

- {{contributor}}{%- endfor %}
  {% endif %}

## Classes

{% for class in onto.classes %}
[{{class.label}}](class/{{class.id}}.md),
{%- endfor %}

## Namepaces

{% for namespace in onto.namespaces%}

- <kbd>{{namespace.prefix}}:</kbd> {{namespace.uri}},
  {%- endfor %}
