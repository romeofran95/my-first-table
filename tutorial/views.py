from django.shortcuts import render
# tutorial/views.py

from django_tables2 import SingleTableView
from django.views.generic import ListView
from .models import Person
from .tables import PersonTable

class PersonListView(SingleTableView):
    model = Person
    table_class=PersonTable
    template_name = 'tutorial/people.html'
