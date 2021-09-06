from django.shortcuts import render

def login(request):
    data = {

    }
    return render(request, 'adminpanel/login.html', data)

def admin(request):
    data = {

    }
    return render(request, 'adminpanel/statistics.html', data)

# Бизнес логика вкладки "Дома"
def house(request):
    data = {

    }
    return render(request, 'adminpanel/house/index.html', data)
