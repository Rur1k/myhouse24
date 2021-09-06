from django.shortcuts import render


def admin(request):
    data = {

    }
    return render(request, 'adminpanel/statistics.html', data)
