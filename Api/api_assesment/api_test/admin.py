from django.contrib import admin
from api_test.models import Catagory,Books,Author


# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Catagory)