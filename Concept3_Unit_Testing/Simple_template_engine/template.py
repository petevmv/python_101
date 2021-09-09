import re
class TemplateEngine:
    def __init__(self, template):
        self.template = template


    def render(self, **context):
        """
        Renders `self.template` by interpolating the variables with data from `context`.

        Raise `TemplatEngineError` if not all variables, present in `self.template`, have values in `context`.
        """
        self.context = context
        pattern = r'({*{[ A-Za-z0-9_ ]+}*.})'
        found_result = re.findall(pattern, self.template)
        if len(found_result) != len(self.context.keys()):
            raise Exception('TemplatEngineError')
        
        text = self.template
        values = [v for k,v in self.context.items()]        
        for idx, el in enumerate(found_result):
            text = text.replace(el, values[idx])
        return text
    
    def extract_variables(self):
        """
        Returns a list of all variables names, that are present in `self.template`
        """
        keys = [k for k,v in self.context.items()]
        return f"{keys}"


template = """
Hello {{ first_name }} {{ last_name }},

I hope this email finds you well.

We are currently running a promotion for {{ product }}.

You can get your discount {{ here }}
"""

engine = TemplateEngine(template)
rendered = engine.render(first_name='Ivan',
    last_name='Ivanov', product='Python course')
print(rendered)
var = engine.extract_variables()
print(var)
