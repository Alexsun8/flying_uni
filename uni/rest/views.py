from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import redirect, render
from idna import unicode

from core.models import Course
from djoser.conf import settings
from rest_framework.generics import get_object_or_404
from rest.serializer import CourseSerializer, ProfileSerializer, UserSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class CoursesJsonView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response({"courses": serializer.data})


class CourseJsonView(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course, many=False)
        return Response({"course": serializer.data})


class ProfileJsonView(APIView):
    def get(self, request, pk):
        log_user = request.user
        user = get_object_or_404(User, pk=pk)
        print(user.pk, log_user.pk)
        print("aten!<",log_user.profile.is_volunteer(),  log_user.pk == user.pk)

        if log_user.pk == user.pk or log_user.profile.is_volunteer():
            serializer = ProfileSerializer(user.profile, many=False)
            return Response({"profile": serializer.data})
        else:
            raise Http404("It's not ur page!")


class ProfilePersonalView(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request):
       user = request.user
       serializer = ProfileSerializer(user.profile, many=False)
       return Response({"profile_personal": serializer.data})

class UserListView(APIView):
    def get(self, request):
        user=request.user
        if not user.profile.is_volunteer():
            raise Http404("U need to be a vol or hi")
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response({"user_list": serializer.data})

# class UserCreate(generics.CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerializer

# class AuthView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'user': unicode(request.user),  # `django.contrib.auth.User` instance.
#             'auth': unicode(request.auth),  # None
#         }
#         return Response(content)
#

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        print("Logout")
        return Response(status=status.HTTP_200_OK)

