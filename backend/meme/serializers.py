from rest_framework import serializers
from meme.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'image', 'author',
                  'content', 'status')
