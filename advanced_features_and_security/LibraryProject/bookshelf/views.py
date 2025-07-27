from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Document
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def documents_list(request):
    douments = Document.objects.all()
    return render(request, 'documents/list.html', {'book_list': douments})

@permission_required('myapp.can_create', raise_exception=True)
def document_create(request):
    if request.method == "POST":
        # Logic to create a new document
        pass
    return render(request, 'documents/create.html')

@permission_required('myapp.can_edit', raise_exception=True)
def document_edit(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    if request.method == "POST":
        # Logic to edit the document
        pass
    return render(request, 'documents/edit.html', {'document': document})

@permission_required('myapp.can_delete', raise_exception=True)
def document_delete(request, document_id):
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect('document_list')


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the valid form data (e.g., save it, use it)
            cleaned_data = form.cleaned_data
            return render(request, 'bookshelf/success.html', {'data': cleaned_data})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/example_form.html', {'form': form})