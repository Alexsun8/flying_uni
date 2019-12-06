from django.db import models
from django.contrib.auth.models import User, Group
from core.models import Course


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    wishes = models.ManyToManyField(Course, blank=True, help_text="Курсы, которые Вы хотите изучать",
                                    related_name="Profile_wishes")
    studying = models.ManyToManyField(Course, blank=True, help_text="Курсы, которые Вы уже изучаете",
                                      related_name="Profile_studying")
    knowledge = models.ManyToManyField(Course, blank=True, help_text="Курсы, которые Вы можете преподавать",
                                       related_name="Profile_knowledge")
    teaching = models.ManyToManyField(Course, blank=True, help_text="Курсы, которые Вы уже преподаёте",
                                      related_name="Profile_teaching")
    contact = models.CharField(max_length=256, help_text="Контакты для связи", verbose_name='Телефон, vk или telegram',
                               default='  ')
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username

    def is_volunteer(self):
        vols = Group.objects.get(name="Volunteers").user_set.all()
        rectors = Group.objects.get(name="Rectors").user_set.all()
        if self.user in vols:
            return True
        if self.user in rectors:
            return True
        return False
