from django.shortcuts import render
# tutorial/views.py

from django_tables2 import SingleTableView
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable
from .tables import PersonFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    template_name = "template.html"
    filterset_class = PersonFilter

class PersonListView(SingleTableView):
    model = Person
    table_class=PersonTable
    template_name = 'tutorial/people.html'


