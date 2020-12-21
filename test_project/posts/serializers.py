from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'text',
            'creation_datetime',
        )

    def validate(self, data):
        validated_data = super().validate(data)
        if validated_data['title'] == 'Serializer Invalid Title':
            raise ValidationError({'title': 'Invalid title at the serializer level.'})
        return validated_data
