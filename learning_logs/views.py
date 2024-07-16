from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """La página de inicio para Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Muestra todos los temas."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Muestra un tema concreto y todas sus entradas."""
    topic = Topic.objects.get(id=topic_id)
    # Asegurarse de que el tema pertenece al usuario actual.
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Añade un nuevo tema."""
    if request.method != 'POST':
        # No se ha enviado datos; se crea un formulario en blanco.
        form = TopicForm()
    else:
        # Se han enviado datos POST; se procesa.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')
    # Mostrar un formulario en blanco o inválido.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Añade una nueva entrada para un tema en concreto."""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # No se ha enviado datos; se crea un formulario en blanco.
        form = EntryForm()
    else:
        # Se han enviado datos POST; se procesa.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    # Mostrar un formulario en blanco o inválido.
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edita una entrada existente."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Se rellena el formulario con la entrada actual.
        form = EntryForm(instance=entry)
    else:
        # Se han enviado datos POST; se procesa.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)