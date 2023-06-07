from django.urls import path
from .views import (
    ProductListCreateAPIView,
    ProductRetrieveUpdateDestroyAPIView,
    ResumeListCreateAPIView,
    ResumeRetrieveUpdateDestroyAPIView,
    CertificateListCreateAPIView,
    CertificateRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('products/', ProductListCreateAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),
    path('resumes/', ResumeListCreateAPIView.as_view(), name='resume-list'),
    path('resumes/<int:pk>/', ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),
    path('certificates/', CertificateListCreateAPIView.as_view(), name='certificate-list'),
    path('certificates/<int:pk>/', CertificateRetrieveUpdateDestroyAPIView.as_view(), name='certificate-detail'),
]