from django.contrib import admin
from shopping import models

for table in models.__all__:

    admin.site.register(getattr(models, table))

