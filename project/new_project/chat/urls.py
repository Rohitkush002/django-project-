from django.urls import path
from . import views as chat_view

urlpatterns = [
    path('', chat_view.index, name='chat')

]