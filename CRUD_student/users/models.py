from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from .choice import BLOOD_CHOICE, DEG_CHOICE, GENDER_CHOICE


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.is_admin


class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    std_name = models.CharField(max_length=120, verbose_name='Student Name')
    std_id = models.CharField(max_length=120, verbose_name='Student ID', primary_key=True)
    contact = models.CharField(max_length=120)
    date_of_birth = models.DateField(null=True)
    blood_group = models.CharField(max_length=100, choices=BLOOD_CHOICE)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    religion = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.std_name


class Teacher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    teacher_name = models.CharField(max_length=120, verbose_name='Teacher Name')
    teacher_initial = models.CharField(max_length=120, unique=True)
    teacher_id = models.CharField(max_length=120, verbose_name='Teacher ID')
    contact = models.CharField(max_length=120)
    salary = models.FloatField()
    designation = models.CharField(max_length=120, choices=DEG_CHOICE)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=100, choices=BLOOD_CHOICE)
    gender = models.CharField(max_length=100, choices=GENDER_CHOICE)
    religion = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_name
