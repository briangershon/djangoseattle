'''
Render form in a CSS friendly way
'''
from django.template import Library
from dssite.models import MenuItem

register = Library()

@register.inclusion_tag('templatetags/nav_bar.html')
def print_navbar():

    return {'menu_items': MenuItem.objects.all().order_by('placement')}
