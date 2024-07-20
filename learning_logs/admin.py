from django.contrib import admin
from .models import Topic, Entry

admin.site.site_header = 'Learning Log Admin'
admin.site.site_title = 'Learning Log Admin'
admin.site.index_title = 'Bienvenido a la administración de Learning Log'
admin.site.site_url = '/'

admin.site.register(Topic)
admin.site.register(Entry)