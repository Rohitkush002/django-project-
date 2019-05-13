from django.shortcuts import render, redirect
from .models import Chat
from .forms import ChatForm


def index(request):
    if not request.session.get('username', None):
        return redirect('login')
    myuser = request.session.get('username', None)
    print(myuser, type(myuser))
    chat = Chat.objects.all().order_by('-date')[10:]
    form = ChatForm(request.POST)
    if request.method == 'POST':

        form = ChatForm(request.POST)
        if form.is_valid():
            user_name = request.session.get('username')

            message = form.cleaned_data.get('message')
            form = Chat(user_name=user_name, message=message)

            form.save()
    data = {
        'chat': chat,
        'form': form,
        'myuser': myuser
    }

    return render(request, "chat.html", data)
