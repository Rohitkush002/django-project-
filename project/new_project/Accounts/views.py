from django.shortcuts import render, redirect
from .models import NewUsers
from .forms import UserForm, ChangePassword, LoginForm

from django.contrib.auth import logout


class UserAccounts:
    def all_users(request):
        if not request.session.get('username', None):
            return redirect('login')
        u = request.session.get('username')
        print(u, type(u))
        users = NewUsers.objects.get(username=u)
        context = {
            'user': users
        }
        return render(request, 'accounts/index.html', context)

    def add_user(request):

        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()

            return redirect('all-users')

        context = {
            'form': form
        }
        return render(request, 'accounts/adduser.html', context)

    def update_user(request, id):
        if not request.session.get('username', None):
            return redirect('login')
        users = NewUsers.objects.get(id=id)
        form = UserForm(request.POST or None, instance=users)
        if form.is_valid():
            form.save()

            return redirect('all-users')

        context = {
            'form': form,
            'users': users
        }
        return render(request, 'accounts/adduser.html', context)

    def delete_user(request, id):
        if not request.session.get('username', None):
            return redirect('login')
        users = NewUsers.objects.get(id=id)
        if request.method == 'POST':
            users.delete()
            return redirect('all-users')

        context = {

            'users': users
        }
        return render(request, 'accounts/confirm_delete.html', context)

    def change_password(request):
        form = ChangePassword()

        if request.method == 'POST':
            password = request.POST['password']
            newPassword = request.POST['newPassword']
            try:
                check = NewUsers.objects.get(password=password)
                if check:
                    chpw = ChangePassword(password=newPassword)
                    chpw.save()
                    print("Password Changed")
            except:
                print("Old Password Not Match")
        context = {

            'form': form
        }
        return render(request, 'accounts/change_password.html', context)

    def login(request):
        if request.session.get('username', None):
            return redirect('login')

        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')

                user_auth = NewUsers.objects.filter(username=username, password=password)
                if user_auth.exists():
                    print("Session:", type(request.session))
                    request.session['username'] = username
                    return redirect('chat')

        data = {
            "form": form
        }
        return render(request, 'accounts/login.html', data)

    def logout_view(request):
        logout(request)

        return redirect('login')
