from rest_framework.serializers import ModelSerializer

from .models import Commentary

class CommentarySerializer(ModelSerializer):
    class Meta:
        model = Commentary
        fields = '__all__'