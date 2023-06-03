import datetime

from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


# Create your models here.

def get_role(user):
    template = ""
    if user.is_authenticated:
        if user.is_superuser:
            template = "teacher"
        elif user.groups.filter(name='teacher').exists():
            template = "teacher"
        elif user.groups.filter(name='student').exists():
            template = "student"
    return template

#Группы
class Groups(models.Model):
    group = models.CharField('Группа', max_length=50, default="")
    spec = models.CharField('Направление', max_length=50, default="")
    num_of_stds = models.IntegerField(default=0)
    offsetName = 0

    names = ["Индекс", "Группа", "Направление", "Кол-во студентов"]
    title = "Группы"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": Disciplines}

    def get_dict(self):
        return {"id": self.id, 0: self.group, 1: self.spec, 2: self.num_of_stds}

    @staticmethod
    def clone():
        return Groups()

    def __str__(self):
        return str(self.id)


#Преподаватели
class Prepods(models.Model):
    prepod_id = models.ForeignKey('ID', on_delete=models.CASCADE, default=0)
    fio = models.CharField("ФИО преподавателя", max_length=150, default="")
    spec = models.CharField("Направление", max_length=150, default="")
    discipline = models.CharField("Дисциплины", max_length=150, default="")
    offsetName = 0

    names = ["Индекс", "ФИО преподавателя", "Направление/профиль", "Дисциплины"]
    title = "Преподаватели"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": Disciplines}

    def get_dict(self):
        return {"id": self.id, 0: self.fio, 1: self.spec, 2: self.discipline}

    @staticmethod
    def clone():
        return Prepods()

    def __str__(self):
        return str(self.prepod_id)



#Дисциплины
class Disciplines(models.Model):
    name = models.CharField("Название", max_length=150, default="")
    spec = models.CharField('Направление', max_length=50, default="")
    prepod = models.CharField("ФИО преподавателя", max_length=150, default="")
    offsetName = 0

    names = ["Название", "Направление", "Преподаватели"]
    title = "Дисциплины"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": Prepods}

    def get_dict(self):
        return {"id": self.id, 0: self.name, 1: self.spec, 2: self.prepod}

    @staticmethod
    def clone():
        return Disciplines()

    def __str__(self):
        return str(self.id)


#Студенты
class Students(models.Model):
    FIO = models.CharField("ФИО", max_length=250, default="")
    group = models.CharField('Группа', max_length=50, default="")
    offsetName = 0

    names = ["Номер з/к", "Фио", "Группа"]
    title = "Студенты"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": False, "have_field": False, "field_id": 1, "linked_class": Groups}

    def get_dict(self):
        return {"id": self.id, 0: self.FIO, 1: self.group}

    @staticmethod
    def clone():
        return Students()


    def __str__(self):
        return str(self.id)


#Справки
class Spravki(models.Model):
    date = models.DateTimeField("Дата", default=datetime.datetime(1, 1, 1))
    FIO = models.CharField("ФИО", max_length=250, default="")
    stip = models.IntegerField("Стипендия", default=0)
    dest = models.CharField("Куда направлен", max_length=250, default="")
    offsetName = 0

    names = ["Номер", "Дата", "ФИО студента", "Стипендия", "Куда направлен"]
    title = "Справки из деканата"

    @staticmethod
    def get_on_to_one():
        return {"is_linked": True, "have_field": False, "field_id": 1, "linked_class": Students}

    def get_dict(self):
        return {"id": self.id, 0: self.date, 1: self.FIO, 2: self.stip, 3: self.dest}

    @staticmethod
    def clone():
        return Spravki()

    def __str__(self):
        return str(self.id)


