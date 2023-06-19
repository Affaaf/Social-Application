from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('posttext/', PostViewSet.as_view()),
    path('getallpost/', GetAllPosts.as_view()),
    path('updatepost/<int:pk>', UpdateApiView.as_view()),
    path('deletepost/<int:pk>', DeleteApiView.as_view()),
    path('likepost/', PostLikeViewSet.as_view()),
    path('dislikelikepost/', DislikeLikeViewSet.as_view()),
    

    
    

    
  
      
]