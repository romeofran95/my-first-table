from tutorial.models import Person
Person.objects.all().delete()
Person.objects.bulk_create([Person(name="Francesco",surname="Romeo",posit="PostDoc",university="University of Trento"),Person(name="Giuliano",surname="Romeo",posit="PhD Student",university="University of Turin"),Person(name="Giancarlo",surname="Rinaldo",posit="Researcher",university="University of Messina")])
