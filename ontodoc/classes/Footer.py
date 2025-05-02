from __future__ import annotations
from jinja2 import Template

import datetime

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ontodoc.classes.Ontology import Ontology
    
class Footer:
    def __init__(self, onto: Ontology, template: Template):
        self.template = template
        self.onto = onto
        
    def __str__(self):
        return "\n\n"+self.template.render(
            metadata={'editionDate': datetime.date.today().strftime('%Y-%m-%d')}
        )