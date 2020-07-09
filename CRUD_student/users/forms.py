from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.db import transaction
from django import forms
from django.forms import TextInput, PasswordInput

from users.admin import UserCreationForm
from users.models import MyUser, Student
from .choice import GENDER_CHOICE, BLOOD_CHOICE, YEARS


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9', }))
    std_name = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9', }))
    std_id = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9'}))
    contact = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9'}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS, attrs={'class': "d-inline col-md-2 "
                                                                                               "form-control"}))
    blood_group = forms.CharField(max_length=20, widget=forms.Select(choices=BLOOD_CHOICE,
                                                                     attrs={'class': 'form-control col-md-9'}))
    gender = forms.CharField(max_length=20, widget=forms.Select(choices=GENDER_CHOICE,
                                                                attrs={'class': 'form-control col-md-9'}))
    password1 = forms.CharField(max_length=500, widget=PasswordInput(attrs={'class': 'form-control col-md-9'}))
    password2 = forms.CharField(max_length=500, widget=PasswordInput(attrs={'class': 'form-control col-md-9'}))

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields = ('email', 'std_name', 'std_id', 'contact', 'date_of_birth', 'blood_group',
                  'gender', 'password1', 'password2',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_student = True
        if commit:
            user.save()
        return user


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'class': 'form-control',
                                                       'id': 'username',
                                                       }))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                           'id': 'password',
                                                           }))


class UpdateStudentProfileForm(forms.ModelForm):

    std_name = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9', }))
    contact = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9'}))
    date_of_birth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS, attrs={'class': "d-inline col-md-2 "
                                                                                               "form-control"}))
    blood_group = forms.CharField(max_length=20, widget=forms.Select(choices=BLOOD_CHOICE,
                                                                     attrs={'class': 'form-control col-md-9'}))
    gender = forms.CharField(max_length=20, widget=forms.Select(choices=GENDER_CHOICE,
                                                                attrs={'class': 'form-control col-md-9'}))
    religion = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9', }))
    nationality = forms.CharField(max_length=120, widget=TextInput(attrs={'class': 'form-control col-md-9', }))

    class Meta:
        model = Student
        fields = ('std_name', 'contact', 'date_of_birth', 'blood_group',
                  'gender', 'religion', 'nationality')

    def save(self, user=None):
        user_profile = super(UpdateStudentProfileForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                               'id': 'old_password',
                                                               }))
    new_password1 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                                'id': 'new_password1',
                                                                }))
    new_password2 = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control',
                                                                'id': 'new_password2',
                                                                }))
