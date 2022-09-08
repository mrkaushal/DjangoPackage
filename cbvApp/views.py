import os

from distutils.command.upload import upload
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from cbvApp.models import User
from authApp.models import CustomUser
from django.shortcuts import redirect


# Create your views here.


class UserCreateView(CreateView):
    model = User
    template_name = 'cbvApp/user_create.html'
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']
        upl = request.FILES
        upload = upl['image']
        is_active = request.POST['status']

        username = request.POST['username']
        password = request.POST['password']

        check_email = CustomUser.objects.filter(email=email)
        if check_email:
            return JsonResponse({'exist_email': 1})

        check_username = CustomUser.objects.filter(username=username)
        if check_username:
            return JsonResponse({'exist_username': 1})

        add = User(
            firstName=firstname,
            lastName=lastname,
            email=email,
            phone=phone,
            description=description,
            image=upload,
            is_active=is_active
        )
        add.save()

        role = 1
        aid = add.id

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            email=email,
            role=role,
            aid=aid
        )
        user.save()
        return JsonResponse({'send': 1})


class UserListView(ListView):
    template_name = 'cbvApp/user_list.html'
    model = User


class UserDetailView(DetailView):
    template_name = 'cbvApp/user_detail.html'
    model = User


class UserUpdateView(UpdateView):
    template_name = 'cbvApp/user_update.html'
    model = User
    fields = '__all__'

    def post(self, request, *args, **kwargs):
        cid = self.kwargs.get("pk")

        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']

        user = User.objects.get(id=cid)
        img_path = user.image.path

        try:
            upload = request.FILES['image']
        except:
            pass
        else:
            if os.path.exists(img_path):
                os.remove(img_path)
                user.image = upload
                user.save()

        User.objects.filter(pk=cid).update(
            firstName=firstname,
            lastName=lastname,
            email=email,
            phone=phone,
            description=description
        )
        return redirect('cbvApp:list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'cbvApp/user_list.html'
    success_url = reverse_lazy('cbvApp:list')

    def get(self, request, *args, **kwargs):
        delete_user = User.objects.get(id=self.kwargs.get("pk"))
        delete_user.delete()
        delete_user_model = CustomUser.objects.get(id=self.kwargs.get("pk"))
        delete_user_model.delete()
        return redirect('cbvApp:list')
