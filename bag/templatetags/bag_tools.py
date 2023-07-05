from django import template

# creating custom tags and filters (Django docs)

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity