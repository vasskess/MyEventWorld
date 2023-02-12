from django.template import Library

register = Library()


@register.filter('my_filter')
def my_date_format(date):
    return date.strftime("%d %B %Y/%H:%M.%p")
