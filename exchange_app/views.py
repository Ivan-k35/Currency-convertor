from django.shortcuts import render

# Create your views here.


def exchange(request):
    name = 'Ivan'

    context = {
        'name': name
    }

    return render(request, 'exchange_app/index.html', context)
