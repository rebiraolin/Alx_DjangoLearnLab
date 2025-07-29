from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm, ExampleForm
from django.contrib.auth.decorators import permission_required

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the bookshelf index.")

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list_view(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create_view(request):
    message = 'You can create books!'
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Book created successfully!'
            return redirect('bookshelf:book_list')
        else:
            message = 'Error creating book. Please check your input.'
    else:
        form = BookForm()
    context = {
        'message': message,
        'form': form,
    }
    return render(request, 'bookshelf/book_form.html', context)

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit_view(request):
    return render(request, 'bookshelf/book_form_edit.html', {'message': 'You can edit books!'})

@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete_view(request):
    return render(request, 'bookshelf/book_delete.html', {'message': 'You can delete books!'})

def example_form_view(request):
    """
    View for a simple example form.
    Demonstrates CSRF protection and basic form handling.
    """
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            message = form.cleaned_data['your_message']
            # In a real app, you'd process/save this data.
            # For this example, we'll just show a success message.
            success_message = f"Thanks, {name}! Your message '{message}' has been received."
            return render(request, 'bookshelf/form_example.html', {'form': ExampleForm(), 'success_message': success_message})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})