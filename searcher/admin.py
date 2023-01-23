from django.contrib import admin
from searcher.models import matter, post, image, text

# Register your models here.
admin.site.register(matter)

admin.site.register(post)

admin.site.register(image)

admin.site.register(text)