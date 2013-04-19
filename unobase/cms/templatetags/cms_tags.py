from django import template

from unobase.cms import models

register = template.Library()

@register.inclusion_tag('cms/menu/main_menu.html')
def main_menu(on):
    
    return {'main_menu_items': models.Menu.objects.all(),
            'on': on}
    
@register.inclusion_tag('cms/menu/menu.html')
def menu(menu_id):
    
    return {'menu_items': models.MenuItem.objects.filter(menu__pk=menu_id)}