from rest_framework import serializers
from learning_logs.models import Topic

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'text', 'date_added']
