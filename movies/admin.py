from django.contrib import admin
from movies.models import Review, Movie, Director

admin.site.register(Review)
admin.site.register(Movie)
admin.site.register(Director)
