import os

from distutils.command.upload import upload
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from cbvApp.models import User
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
        
        User.objects.create(
            firstName=firstname, 
            lastName=lastname, 
            email=email, 
            phone=phone, 
            description=description, 
            upload=upload, 
            is_active=is_active
        )
        return redirect('cbvApp:list')

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
        global upload
        cid = self.kwargs.get("pk")
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        description = request.POST['description']
        upl = request.FILES

        old_image = User.objects.get(id=cid)
        print(old_image)
        img_path = old_image.upload.path
        print(img_path)

        if os.path.exists(img_path):
            os.remove(img_path)
            upl = request.FILES
            upload = upl['image']
            print(upload)

        User.objects.filter(pk=cid).update(
            firstName=firstname,
            lastName=lastname,
            email=email,
            phone=phone,
            description=description,
            upload=upload
        )
        return redirect('cbvApp:list')

class UserDeleteView(DeleteView):
    model = User
    template_name = 'cbvApp/user_list.html'
    success_url = reverse_lazy('cbvApp:list')

    def get(self, request, *args, **kwargs):
        self.delete(request)
        return reverse_lazy('cbvApp:list')