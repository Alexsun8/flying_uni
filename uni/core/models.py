from django.db import models


class Location(models.Model):
    address = models.CharField(max_length=256, help_text="Место проведения", verbose_name='Адрес')

    def __str__(self):
        return self.address


class Course(models.Model):
    name = models.CharField(max_length=256, help_text="Название курса", verbose_name='Название курса')

    STATUS_CHOICES = (
        ("started", "Запущен"),
        ("in_progress", "В процессе"),
        ("search", "Набор"),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
