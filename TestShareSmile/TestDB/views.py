from django.shortcuts import render
from rest_framework import viewsets
from serializers import UsersSerializer
from serializers import CausesSerializer,DetailedCausesSerializer
from .models import Users
from .models import Causes
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from serializers import UserInterfaceSerializer
from rest_framework import permissions
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class user_list(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)


class user_detail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserInterfaceSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserInterfaceSerializer


def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


class CausesViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Causes.objects.all().order_by('-date_joined')
    serializer_class = CausesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class causes_list(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    """
    List all code snippets, or create a new snippet.
    """
    queryset = Causes.objects.all()
    serializer_class = CausesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class causes_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a code snippet.
    """
    queryset = Causes.objects.all()
    serializer_class = CausesSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
