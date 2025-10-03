from django.shortcuts import render

# Create your views here.

def index(request):
    productos = [
        {"nombre": "Laptop Gamer", "precio": 1200, "stock": 50},
        {"nombre": "Teclado Mecánico RGB", "precio": 85, "stock": 120},
        {"nombre": "Mouse Inalámbrico", "precio": 45, "stock": 200},
    ]
    contexto = {
        'productos': productos
    }
    return render(request, 'index.html', contexto)
