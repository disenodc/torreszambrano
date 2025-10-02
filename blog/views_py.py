from django.shortcuts import render, redirect
from .models import Post, Autor, Categoria
from .forms import PostForm, AutorForm, CategoriaForm, BuscarForm

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def crear_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'crear_post.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def buscar(request):
    posts = []
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['buscar']
            posts = Post.objects.filter(titulo__icontains=query)
    else:
        form = BuscarForm()
    return render(request, 'buscar.html', {'form': form, 'posts': posts})