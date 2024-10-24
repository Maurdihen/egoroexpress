from django.shortcuts import render

def home(request):
    return render(request, 'home_page/home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Имя: {name}, Телефон: {phone}, Контактный телефон: {message}\n")
    return render(request, 'contact_page/contact.html')