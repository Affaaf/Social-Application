from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, status
from .serializers import PostSerializer,LikeSerializer,PostSendSerializer,LikeCreateSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from user_authentication_app.models import User
from rest_framework.response import Response
from .models import Post,Like

# Create your views here.
#

# Get all Posts
class GetAllPosts(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostViewSet(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    # Get Login Users Posts
    def get(self, request, format=None):
        posts = Post.objects.filter(user=request.user.id)
        if posts.exists():
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'No posts found for the logged-in user.'}) 
     
    # Send a Post By Login User
    def post(self, request, format=None):

        serializer = PostSendSerializer(data=request.data)
        
        if serializer.is_valid():
                serializer.save(user=request.user)  
                return Response(serializer.data,status=201)
        else:
            return Response(serializer.errors, status=400)
        


# Delete a Post 
class DeleteApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def delete(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found against this user'}, status=404)

        post.delete()
        return Response(status=204)
    


# For Update posts
class UpdateApiView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request, pk=None):
        try:
            post = Post.objects.get(pk=pk, user=request.user)
        except Post.DoesNotExist:
            return Response({'message': 'Post not found against this user'}, status=404)

        serializer = PostSendSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
    


# For Like posts
class PostLikeViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        user = request.user
        user_id = user.id
        
        try:
            post = Post.objects.get(id=post_id)
            total_like=post.like
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=404)

        try:
            existing_like = Like.objects.get(post=post, user=user)
            return Response({'detail': 'You have already liked this post.'}, status=400)
        
        except Like.DoesNotExist:
            total_like=total_like+1
            post.like=total_like
            post.save()
            print("Total like=====",total_like)
            serializer = LikeCreateSerializer(data={'post': post_id, 'user': user_id, 'is_active': 1,'like':total_like})
            if serializer.is_valid():
                serializer.save()
                return Response({'massage': 'Post liked saved successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({"massages": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



# For Dislike  Posts
class DislikeViewSet(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        post_id = request.data.get('post_id')
        user = request.user
       
        try:
            post = Post.objects.get(id=post_id)
            total_like=post.like
            print("likes============",total_like)
        except Post.DoesNotExist:
            return Response({'detail': 'Post not found.'}, status=404)

        try:
            existing_like = Like.objects.get(post=post, user=user)
            existing_like.delete()
            if total_like == 0:
                total_like=0
            else:
                total_like=total_like-1
            post.like=total_like
            post.save()
            return Response(status=204)
        
        except Like.DoesNotExist:
            return Response({'detail': 'You have not like this post.'}, status=400)
            