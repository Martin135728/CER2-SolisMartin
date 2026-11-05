from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .models import Categoria, LugarPatrimonial

def principal(request):
    return render(request, 'core/principal.html')

def catalogo(request):
    list_categorias = Categoria.objects.all().order_by('nombre')
    categoria_id = request.GET.get('categoria')

    if categoria_id:
        list_lugares = LugarPatrimonial.objects.filter(categoria__id=categoria_id)
    else:
        list_lugares = LugarPatrimonial.objects.all().order_by('nombre')

    data = {
        'categorias': list_categorias,
        'lugares': list_lugares
    }
    return render(request, 'core/catalogo.html', data)

def vista_individual(request, pk):
    lugar = get_object_or_404(LugarPatrimonial, pk=pk)

    data = {
        'lugar': lugar
    }

    return render(request, 'core/vista_individual.html', data)

def login_view(request):
    if request.method == 'POST':   
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('principal')
        else:
            error_message = 'Nombre de usuario o contraseña incorrectos.'
            return render(request, 'core/login.html', {'error_message': error_message})
    
    return render(request, 'core/login.html')

def logout_view(request):
    auth_logout(request)
    return redirect('principal')

@login_required
def crear_lugar_view(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        ubicacion = request.POST.get('ubicacion')
        anio_construccion = request.POST.get('anio_construccion')
        categoria_id = request.POST.get('categoria')

        categoria = get_object_or_404(Categoria, id=categoria_id)

        lugar = LugarPatrimonial(
            nombre=nombre,
            descripcion=descripcion,
            ubicacion=ubicacion,
            anio_construccion=anio_construccion,
            categoria=categoria
        )
        lugar.save()

        return redirect('catalogo')

    categorias = Categoria.objects.all()
    return render(request, 'core/crear_lugar.HTML', {'categorias': categorias})