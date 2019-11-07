from django.contrib.auth.forms import AuthenticationForm
from django.db import models
from django.forms import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
# from django.contrib.auth.models import AbstractUser



class Location(models.Model):
    address = models.CharField(max_length=256, help_text="Место проведения", verbose_name='Адрес',
                               default="Место проведения  не найдено")
    name = models.CharField(max_length=256, help_text="Те, кто предоставили место проведения",
                            verbose_name='Название организации или имя владельца помещения',
                            default="Место проведения  не найдено")
    contact = models.CharField(max_length=256, help_text="Контакты для связи", verbose_name='Телефон, vk или telegram',
                               default="Место проведения  не найдено")

    def __str__(self):
        return self.address


class President(models.Model):
    name = models.CharField(max_length=128, help_text="Ответственный за курс", verbose_name="Староста курса",
                            default="Староста не найден(а)")
    telephone = models.CharField(max_length=64, help_text="Номер для связи", verbose_name="Номер телефона",
                                 default="Староста не найден(а)")
    vk_id = models.CharField(max_length=64, help_text="вк дл связи", verbose_name="Vk.id", blank=True, null=True)
    email = models.CharField(max_length=64, help_text="Адрес электронной почты для связи", verbose_name="email address",
                             blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=256, help_text="Название курса", verbose_name='Название курса')

    STATUS_CHOICES = (
        ("done", "Запущен"),
        ("in_progress", "В процессе"),
        ("teachers", "Поиск преподавателя"),
        ("place", "Поиск места проведения"),
        ("te_and_pl", "Поиск места проведения и преподавателя"),
        ("president", "Выборы старосты"),
        ("students", "Набор людей"),
    )

    #  TYPE_CHOICES = (

    # )

    # TYPE_CHOICES = ()

    status = models.CharField(choices=STATUS_CHOICES, max_length=16)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    group_president = models.ForeignKey(President, on_delete=models.PROTECT, blank=True, null=True)
    date = models.DateField(help_text="Дата подвешивания курса", blank=True, null=True)
    information = models.TextField(max_length=1000, help_text="Краткая информация о курсе", blank=True, null=True)

    # type =
    # level =

    def __str__(self):
        return f"{self.name} - {self.status}"


class News(models.Model):
    headline = models.CharField(max_length=100, help_text="Заголовок", verbose_name="Основная суть, объявление",
                                default="Внимание!")
    date = models.DateField(auto_now=True, help_text="Время объявления")
    message = models.TextField(max_length=5000, help_text="Сама новость", blank=True, null=True)

    def __str__(self):
        return self.headline



#    @receiver(post_save, sender=User)
 ##   def create_user_profile(sender, instance, created, **kwargs):
     #   if created:
    #        Profile.objects.create(user=instance)

   # @receiver(post_save, sender=User)
  #  def save_user_profile(sender, instance, **kwargs):
 #       instance.profile.save()
#
    # def __str__(self):
    #     return 'Profile for user {}'.format(self.user.username)

