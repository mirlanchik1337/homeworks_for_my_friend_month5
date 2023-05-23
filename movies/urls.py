from django.urls import path
from movies.views import *

urlpatterns = [
    path('api/v1/directors/', director_list),
    path('api/v1/directors/<int:id>/', get_director),
    path('api/v1/movies/', movie_list),
    path('api/v1/movies/<int:id>/', get_movie),
    path('api/v1/reviews/', review_list),
    path('api/v1/reviews/<int:id>/', get_review),
]
