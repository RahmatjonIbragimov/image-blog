from django.urls import path
from .views import *

urlpatterns = [
    path('', BlockPageView.as_view(), name='main'),
    path('block/<str:slug>/', SingView.as_view(), name='page'),
    path('tag/<str:slug>/', TagView.as_view(), name='Tag'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<str:slug>/', CategoryView.as_view(), name='category')
]
