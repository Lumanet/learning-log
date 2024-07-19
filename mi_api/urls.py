from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('entradas', views.EntryViewSet, basename='entradas')

urlpatterns = [
    path('topics-list/', views.TopicAPIList.as_view(), name='topic_list'),
    path('topics-entradas/', views.TopicAPIListConEntradas.as_view(), name='topic_entradas'),
    path('topics-create/', views.TopicAPICreate.as_view(), name='topic_create'),
    path('topics-retrieve/<int:pk>/', views.TopicAPIRetrieve.as_view(), name='topic_retrieve'),
]

urlpatterns += router.urls 
