from django.core.validators import validate_email
from rest_framework import serializers
from .models import Post,Like
from user_authentication_app.serializers import SignupSerializer


class LikeSerializer(serializers.ModelSerializer):

    user = SignupSerializer
    
    class Meta:
        model = Like
        fields = fields ="__all__"


class PostSerializer(serializers.ModelSerializer):

    user = SignupSerializer
    post_like_related = LikeSerializer

    class Meta:
        model = Post
        fields = ('id','post_text','like','user','post_like_related')
    
    
class PostSendSerializer(serializers.ModelSerializer):

    user = SignupSerializer

    class Meta:
        model = Post
        fields = fields ="__all__"


class LikeCreateSerializer(serializers.ModelSerializer):

    user = SignupSerializer
    post = PostSendSerializer

    class Meta:
        model = Like
        fields = fields ="__all__"