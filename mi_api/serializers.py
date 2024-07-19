from rest_framework import serializers
from learning_logs.models import Topic, Entry

# Serializador de modelo
class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'
        # fields = ['id', 'text', 'date_added']
        
class TopicConEntradasSerializer(serializers.ModelSerializer):
    entradas = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='entradas-detail')
    
    class Meta:
        model = Topic
        fields = '__all__'
        # fields = ['id', 'text', 'date_added', 'entradas']
        
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'
        # fields = ['id', 'text', 'date_added']