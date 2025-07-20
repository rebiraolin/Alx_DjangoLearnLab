from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView # <--- Added CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # <--- Added reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin # <--- Added LoginRequiredMixin, PermissionRequiredMixin
from .models import Book, Library, UserProfile, Author # <--- Ensure Author is imported for Book forms
from .forms import UserRegisterForm # Assuming you have this
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test


# Helper functions for role checking (keep these as they are for Task 3)
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Existing views (book_list, LibraryDetailView, register, home, admin_view, librarian_view, member_view)
def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('relationship_app:login')
    else:
        form = UserRegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})


def home(request):
    return render(request, 'relationship_app/home.html')


@login_required
@user_passes_test(is_admin, login_url='/library/login/', redirect_field_name=None)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian, login_url='/library/login/', redirect_field_name=None)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member, login_url='/library/login/', redirect_field_name=None)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# --- New Views for Book Operations with Custom Permissions ---

# For `CreateView`, `UpdateView`, `DeleteView`, you need to specify `model`, `fields`, and `success_url`.
# `fields = '__all__'` is used here for simplicity. In a real app, you'd list specific fields.

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author'] # Specify fields for the form
    template_name = 'relationship_app/book_form.html' # We'll create this template
    success_url = reverse_lazy('relationship_app:book_list') # Redirect to book list after success
    permission_required = 'relationship_app.can_add_book' # Apply the custom permission

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html' # Use the same form template
    success_url = reverse_lazy('relationship_app:book_list')
    permission_required = 'relationship_app.can_change_book' # Apply the custom permission

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html' # We'll create this template
    success_url = reverse_lazy('relationship_app:book_list')
    permission_required = 'relationship_app.can_delete_book' # Apply the custom permission