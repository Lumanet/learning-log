from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registra un nuevo usuario."""
    if request.method != 'POST':
        # Muestra un formulario en blanco.
        form = UserCreationForm()
    else:
        # Procesa el formulario completado.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Inicia la sesión y redirige a la página principal.
            login(request, new_user)
            return redirect('learning_logs:index')
    
    # Muestra un formulario en blanco o inválido.
    context = {'form': form}
    return render(request, 'registration/register.html', context)


