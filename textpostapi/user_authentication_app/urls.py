from django.urls import path
from .import views
from .views import *


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginAPIView.as_view()),
    
    
     
    
    
   
    
    
     


      
]