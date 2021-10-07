import ipdb
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
        for k, v in self.context.items():
            if type(v) is int:
                raise TypeError('end result is string object, insted int is given...')
                break

        pattern = r'({{[A-Za-z0-9_ ]+}})'
        pattern_no_brackets = r'{{([ A-Za-z0-9_ ]+)}}'
        found_result = re.findall(pattern, self.template)
        found_result_no_brackets = re.findall(pattern_no_brackets, self.template)
        
        for el in found_result_no_brackets:
            if el.strip() not in self.context:
                raise TypeError('TemplatEngineError')

        text = self.template
        
        for el in found_result:
            # ipdb.set_trace()
            for k, v in self.context.items():
                if k in [x.strip() for x in re.findall(pattern_no_brackets, el)]:
                    # print(k, v , 'element:', el)
                    text = text.replace(el, v)
                    break


        return text
    
    def extract_variables(self):
        """
        Returns a list of all variables names, that are present in `self.template`
        """
        pattern = r'{{([ A-Za-z0-9_ ]+)}}'
        found_result = re.findall(pattern, self.template)
        
        return [x.strip() for x in found_result]


        

template = """
Hello {{ first_name }} {{ last_name }},

I hope this email finds you well.

We are currently running a promotion for {{ product }}.

You can get your discount {{ here }}
"""

engine = TemplateEngine(template)
rendered = engine.render(first_name='Ivan',
    last_name='Ivanov', product='Python course', here='https:alabal')
print(rendered)
var = engine.extract_variables()
print(var)
other_template = "Hello there, {{ x }}"
engine_new = TemplateEngine(other_template)
rendered_new = engine_new.render(x='General Kenobi.')
print(rendered_new)
variables = engine_new.extract_variables()
print(variables)
a = TemplateEngine('x {{ x  }}, y {{x}}, z {{x}}')
 
print(a.render(x='1'))
print(a.extract_variables())

