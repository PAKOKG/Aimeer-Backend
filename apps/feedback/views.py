from rest_framework import generics
from .models import Feedback, ConnectWithUs
from .serializers import FeedbackSerializer, ConnectWithUsSerializer


class FeedbackListCreateAPIView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class ConnectWithUsListCreateAPIView(generics.ListCreateAPIView):
    queryset = ConnectWithUs.objects.all()
    serializer_class = ConnectWithUsSerializer


class ConnectWithUsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConnectWithUs.objects.all()
    serializer_class = ConnectWithUsSerializer
