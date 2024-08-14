from django import template
from django.urls import resolve
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu = Menu.objects.get(name=menu_name)
    menu_items = menu.items.select_related('parent').all()

    def build_tree(items, parent=None):
        tree = []
        for item in items:
            if item.parent == parent:
                children = build_tree(items, item)
                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': current_url == item.get_url(),
                })
        return tree

    tree = build_tree(menu_items)

    return {
        'menu_tree': tree,
        'current_url': current_url,
    }
