from django.shortcuts import render, HttpResponse


def register(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        reg = register(name=name, email=email, password=password)
        reg.save()
    return render(request, 'register.html')


def login(request):
    return HttpResponse('Working Again')

# Create your views here.
