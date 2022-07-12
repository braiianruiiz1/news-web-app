from django.urls import path
from .views import NewListView, NewDetailView, NewCreate, NewUpdate, NewDelete

news_patterns = ([
    path('', NewListView.as_view(), name='news'),
    path('<int:pk>/<slug:new_slug>/', NewDetailView.as_view(), name='new'),
    path('create/', NewCreate.as_view(), name='create'),
    path('update/<int:pk>', NewUpdate.as_view(), name='update'),
    path('delete/<int:pk>', NewDelete.as_view(), name='delete'),
], 'news')