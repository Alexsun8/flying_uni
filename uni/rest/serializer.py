from django.contrib.auth.models import User
from account.models import Profile
from core.models import Course, Location, Categories
from rest_framework import serializers


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    domain = serializers.ChoiceField(Categories.DOMAIN_CHOIСES)

    class Meta:
        model = Categories
        fields = ('name', 'domain',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        extra_kwargs = {'password': {'write_only': True}}


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'address', 'contact',)


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    status = serializers.ChoiceField(Course.STATUS_CHOICES)
    location = LocationSerializer()
    group_president = UserSerializer()
    teacher = UserSerializer()
    type = CategoriesSerializer()

    class Meta:
        model = Course
        fields = ('name', 'information', 'date', 'status', 'location', 'group_president', 'teacher', 'type', 'pk',)

    def get_quaryset(self):
        return Course.objects.all()


class CourseShortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'pk',)

    def get_quaryset(self):
        return Course.objects.all()


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    wishes = CourseShortSerializer(many=True)
    studying = CourseShortSerializer(many=True)
    knowledge = CourseShortSerializer(many=True)
    teaching = CourseShortSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'wishes', 'studying', 'knowledge', 'teaching', 'contact', 'birth_date',)
