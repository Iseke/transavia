from django.urls import path

from avia import views

urlpatterns = [
    path('search/', views.SearchView.as_view())
]