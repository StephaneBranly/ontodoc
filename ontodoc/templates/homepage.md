# {{onto.label}}

{{onto.comment}}

## Contributors

{% for contributor in onto.contributors%}

- {{contributor}}{%- endfor %}

## Classes

{% for class in onto.classes %}
[{{class.label}}](class/{{class.id}}.md),
{%- endfor %}

## Namepaces

{% for namespace in onto.namespaces%}

- <kbd>{{namespace.prefix}}:</kbd> {{namespace.uri}},
  {%- endfor %}
