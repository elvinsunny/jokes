# # urls.py
# from django.urls import path
# from .views import JokesByLanguageAPIView, AddJokeAPIView, LanguagesAPIView

# urlpatterns = [
#     path('api/languages/', LanguagesAPIView.as_view(), name='languages'),
#     path('api/jokes/<str:language>/', JokesByLanguageAPIView.as_view(), name='jokes_by_language'),
#     path('api/add_joke/', AddJokeAPIView.as_view(), name='add_joke'),
# ]


# urls.py
# from django.urls import path
# from .views import JokesByLanguageAPIView, AddJokeAPIView, LanguagesAPIView, AllJokesAPIView, DeleteJokeAPIView, UpdateJokeAPIView

# urlpatterns = [
#     path('api/languages/', LanguagesAPIView.as_view(), name='languages'),
#     path('api/jokes/<str:language>/', JokesByLanguageAPIView.as_view(), name='jokes_by_language'),
#     path('api/add_joke/', AddJokeAPIView.as_view(), name='add_joke'),
#     path('api/all_jokes/', AllJokesAPIView.as_view(), name='all_jokes'),
#     path('api/delete_joke/<int:joke_id>/', DeleteJokeAPIView.as_view(), name='delete_joke'),
#     path('api/update_joke/<int:joke_id>/', UpdateJokeAPIView.as_view(), name='update_joke'),  # New URL pattern
# ]


# from django.urls import path

# from .views import *

# urlpatterns = [
#     path('api/languages/', LanguagesAPIView.as_view(), name='languages'),
#     path('api/jokes/', JokeListCreate.as_view(), name='joke-list-create'),
#     path('api/jokes/<int:pk>/', JokeDetail.as_view(), name='joke-detail'),
# ]


# urls.py

from django.urls import path
from .views import JokeListCreate, JokeDetail, LanguagesAPIView

urlpatterns = [
    path('api/languages/', LanguagesAPIView.as_view(), name='languages'),
    path('api/jokes/', JokeListCreate.as_view(), name='joke-list-create'),
    path('api/jokes/<str:language>/', JokeListCreate.as_view(), name='joke-list-by-language'),
    path('api/jokes/<int:pk>/', JokeDetail.as_view(), name='joke-detail'),
]


