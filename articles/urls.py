from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    # create
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),

    # comment
    # create
    path('<int:id>/comments/create/', views.comment_create, name='comment_create'),
]