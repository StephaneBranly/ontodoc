from jinja2 import Template

import datetime
    
class Footer:
    def __init__(self, onto, template: Template):
        self.template = template
        self.onto = onto
        
    def __str__(self):
        return "\n\n"+self.template.render(
            # onto=self.onto.__dict__,
            metadata={'editionDate': datetime.date.today().strftime('%Y-%m-%d')}
        )