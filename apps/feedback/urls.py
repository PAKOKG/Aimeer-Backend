from django.urls import path
from .views import (
    FeedbackListCreateAPIView,
    FeedbackRetrieveUpdateDestroyAPIView,
    ConnectWithUsListCreateAPIView,
    ConnectWithUsRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('feedback/', FeedbackListCreateAPIView.as_view(), name='feedback-list'),
    path('feedback/<int:pk>/', FeedbackRetrieveUpdateDestroyAPIView.as_view(), name='feedback-detail'),
    path('connect-with-us/', ConnectWithUsListCreateAPIView.as_view(), name='connect-with-us-list'),
    path('connect-with-us/<int:pk>/', ConnectWithUsRetrieveUpdateDestroyAPIView.as_view(), name='connect-with-us-detail'),
]