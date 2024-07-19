from django.shortcuts import render
from rest_framework import generics, viewsets
from learning_logs.models import Topic, Entry
from .serializers import TopicSerializer, EntrySerializer, TopicConEntradasSerializer

# Create your views here.
class TopicAPIList(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
class TopicAPIListConEntradas(generics.ListAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicConEntradasSerializer
    
class TopicAPICreate(generics.CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
class TopicAPIRetrieve(generics.RetrieveAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    
# ViewSets
class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer