from django.shortcuts import render
import requests


def exchange(request):
    url = 'https://api.exchangerate.host/latest'
    params = {
        'base': 'USD',
        'symbols': ['USD,EUR,RUB']
    }

    response = requests.get(url, params=params).json()
    currencies = response.get('rates')

    if request.method == 'GET':

        context = {
            'currencies': currencies
        }

        return render(request, 'exchange_app/index.html', context)

    if request.method == 'POST':
        if request.POST.get('from-amount'):
            from_amount = request.POST.get('from-amount')
        else:
            from_amount = 0
        from_curr = request.POST.get('from-curr')
        to_curr = request.POST.get('to-curr')

        converted_amount = round((currencies[to_curr] / currencies[from_curr]) * float(from_amount), 2)

        context = {
            'from_curr': from_curr,
            'to_curr': to_curr,
            'from_amount': from_amount,
            'currencies': currencies,
            'converted_amount': converted_amount
        }

        return render(request, 'exchange_app/index.html', context)
