from django import template

register = template.Library()

CURRENCY_SYMBOLS = {
    'eur': '€',
    'usd': '$',
    'rub': 'P',
}

@register.filter()
def currency(value, code='eur'):
    """
    value: значение, к которому нужно применить фильтр
    code: код валюты
    """
    postfix = CURRENCY_SYMBOLS[code]

    return f'{value} €'