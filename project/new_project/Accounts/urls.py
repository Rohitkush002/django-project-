

from django.urls import path,include

from .views import UserAccounts


urlpatterns = [

    path('',UserAccounts.all_users, name='all-users'),
    path('newuser/',UserAccounts.add_user, name='new-user'),
    path('login/',UserAccounts.login, name='login'),
    path('logout/',UserAccounts.logout_view, name='logout'),
    path('changepassword/',UserAccounts.change_password, name='change_password'),
    path('update/<int:id>',UserAccounts.update_user, name='update_user'),
    path('delete/<int:id>',UserAccounts.delete_user, name='delete_user'),



]