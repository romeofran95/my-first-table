import django_tables2 as tables
from .models import Person
from django.utils.html import format_html
import django_filters

class PersonTable(tables.Table):
    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
        fields = ("name", "surname","posit","university",)
def render_name(self, value, record):
        return format_html("<b>{} {}</b>", value, record.surname)
def render_count(self, value):
    if self.request.user.is_authenticated():
        return value
    else:
        return '---'

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'posit']
