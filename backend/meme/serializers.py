from rest_framework import serializers
from meme.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'category', 'image', 'author',
                  'excerpt', 'content', 'status')

