# {{onto.label}}

{{onto.comment}}

## Contributors

{% for contributor in onto.contributors%}

- {{contributor}}{%- endfor %}

## Classes

{% for class in onto.classes %}
[{{class.label}}](class/{{class.id}}.md),
{%- endfor %}
