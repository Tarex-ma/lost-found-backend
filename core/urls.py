from django.urls import path 
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView 
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),

    path('lost-items/', LostItemListCreateView.as_view()),
    path('lost-items/<int:pk>/', LostItemDetailView.as_view()),

    path('found-items/', FoundItemListCreateView.as_view()), 
    path('claims/', ClaimRequestCreateView.as_view()),
    path('claims/<int:pk>/approve/', ApproveClaimView.as_view()),
    path('claims/<int:pk>/reject/', RejectClaimView.as_view()),
    path('found-items/<int:pk>/matches/', FoundItemMatchView.as_view()),
]