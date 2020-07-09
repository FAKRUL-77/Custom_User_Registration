from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

# Create your views here.

from users.forms import StudentSignUpForm, UserLoginForm, UpdateStudentProfileForm, UserPasswordChangeForm
from users.models import MyUser, Student


def home(request):
    return render(request, 'users/home_page.html')


class StudentSignUpView(CreateView):
    model = MyUser
    form_class = StudentSignUpForm
    template_name = 'users/student_signup_form.html'

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        user.refresh_from_db()
        std_id = form.cleaned_data.get('std_id')
        student = Student.objects.create(user=user, pk=std_id)
        student.std_name = form.cleaned_data.get('std_name')
        student.contact = form.cleaned_data.get('contact')
        student.date_of_birth = form.cleaned_data.get('date_of_birth')
        student.blood_group = form.cleaned_data.get('blood_group')
        student.gender = form.cleaned_data.get('gender')
        student.save()

        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return redirect('home')


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'users/user_login.html'
    success_message = 'You are successfully logged in'


class UserLogoutView(LogoutView):
    template_name = 'users/home_page.html'
    next_page = 'home'


class StudentProfileView(DetailView):
    model = MyUser
    template_name = 'users/profile_page.html'
    context_object_name = 'student'


class UpdateStudentProfileView(UpdateView):
    model = MyUser
    form_class = UpdateStudentProfileForm
    # success_message = 'You are successfully update your profile !!'
    template_name = "users/update_student_profile.html"

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(MyUser, pk=self.kwargs['pk'])
        return user.student

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': userid})


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_message = 'You are successfully update your profile !!'
    template_name = 'users/password_change_form.html'

    def get_success_url(self):
        userid = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': userid})

