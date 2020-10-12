from django.urls import path, include
from api_basics.views import article_list,article_details

urlpatterns = [
    path('article/', article_list),
    path('article/<int:pk>/',article_details),
    
]