'''
Render form in a CSS friendly way
'''
from django.template import Library
register = Library()

@register.inclusion_tag('templatetags/print_form.html')
def print_form(form, show_required = False):
    result_list = []
    for field_name, field in form.fields.items():
        classes = ' '.join((type(field).__name__,
                           type(field.widget).__name__,
                           u'required' if field.required else u'optional'),)
        context = {'field':form[field_name], 'name':field_name, 'classes':classes, 'required':field.required}

        context['required'] = field.required if show_required else False
            
        result_list.append(context)

    return {'fields': result_list}
