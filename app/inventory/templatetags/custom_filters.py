from django import template
from django.contrib.auth.models import Group

# Создание объекта для регистрации фильтров и тегов
register = template.Library()

# Реализация фильтра
@register.filter
def belongs_to_group(user, Editors):
    return user.groups.filter(name=Editors).exists()