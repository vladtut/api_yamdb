from django.shortcuts import render
from rest_framework import viewsets
from .permissions import IsRoleUser
from .serializers import CommentSerializer, ReviewSerializer
from rest_framework import permissions


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (
        IsRoleUser, permissions.IsAuthenticatedOrReadOnly)
# Create your views here.


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = (
        IsRoleUser, permissions.IsAuthenticatedOrReadOnly)