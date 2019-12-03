import this

from django.contrib.auth.models import User
from django.db import models
from requests import auth


class Location(models.Model):
    address = models.CharField(max_length=256, help_text="Подробно: город, улица, дом, подъезд/вход, квартира/помещение", verbose_name='Адрес')
                               # default="Место проведения  не найдено")
    name = models.CharField(max_length=256, help_text="Те, кто предоставили место проведения",
                            verbose_name='Название организации или имя владельца помещения',)
                            # default="Место проведения  не найдено")
    contact = models.CharField(max_length=256, help_text="Контакты для связи", verbose_name='Телефон, vk или telegram',)
                               # default="Место проведения  не найдено")

    def __str__(self):
        return self.address



class Categories(models.Model):
    name = models.CharField(max_length=100, help_text="Название подкатегории",
                            default="Другое")
    DOMAIN_CHOIСES = (
        ("Art", "Творчество"),
        ("Needlework", "Рукоделие"),
        ("Technical", "Технические"),
        ("Medicine", "Химбио"),
        ("Humanities", "Гумаитарные"),
        ("Alternative", "Другие"),
    )

    domain = models.CharField(choices=DOMAIN_CHOIСES, max_length=16)

    def __str__(self):
        return self.name

class Course(models.Model):
    class Meta:
        # делает уникальным направление обмена
        unique_together = ("group_president", "teacher",)

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

    status = models.CharField(choices=STATUS_CHOICES, max_length=16)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    # group_president = models.ForeignKey(President, on_delete=models.PROTECT, blank=True, null=True)
    group_president = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, help_text="Староста",
                                        related_name='user_group_president')
    date = models.DateField(help_text="Дата подвешивания курса", blank=True, null=True)
    information = models.TextField(max_length=1000, help_text="Краткая информация о курсе", blank=True, null=True)
    teacher = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, null=True, help_text="Преподаватель курса",
                                related_name='user_teacher')

    type = models.ForeignKey(Categories, blank=True, on_delete=models.PROTECT, null=True, help_text="Категория курса",
                                related_name='type_teacher')

    def __str__(self):
        return self.name

    def has_teacher(self):
        # print("Course ", self.name)
        # print("Teachers: ", self.teacher)
        if self.teacher is None:
            # print("hasn't teacher")
            return False
        # print("has teacher")
        return True


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



