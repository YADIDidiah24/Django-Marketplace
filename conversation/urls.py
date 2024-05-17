from django.urls import path

from . import views

app_name = 'conversation'

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path('conversations/<int:item_pk>/', views.newConversation, name='new'),
    path('<int:pk>/', views.detail, name='detail'),

]