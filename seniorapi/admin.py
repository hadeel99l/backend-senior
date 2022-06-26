from django.contrib import admin
from .models import number, users, car, Stream, pat_ref
# Register your models here.
admin.site.register(users)
admin.site.register(Stream)
admin.site.register(number)
admin.site.register(car)
admin.site.register(pat_ref)