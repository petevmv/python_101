class TemplateEngine:
    def __init__(self, template):
        self.template = template


    def render(self, **context):
        """
        Renders `self.template` by interpolating the variables with data from `context`.

        Raise `TemplatEngineError` if not all variables, present in `self.template`, have values in `context`.
        """
        self.context = context
        bracket_location = self.template.find('{')
        greet = template[:bracket_location]
        list_of_args = [x for x in template[bracket_location:] if x not in ('{', '}',' ')]
        return f"{greet}{self.context[list_of_args[0]]}"

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
rendered = engine.render(x='General Kenobi.')
print(rendered)
var = engine.extract_variables()
print(var)
