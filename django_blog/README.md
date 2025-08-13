Django Blog Project – Authentication System and Post Management
Project Overview
This repository contains the code for a Django blog project, developed as part of the Alx_DjangoLearnLab curriculum.

The first phase focused on a secure and user-friendly authentication system. The second phase introduces a full post management system with CRUD (Create, Read, Update, Delete) functionality.

Authentication System Features
The authentication system combines Django's built-in authentication tools with custom views and forms to enhance functionality and user experience.

User Registration – UserRegistrationForm extends Django's default user creation form to include an email field.

Login & Logout – Uses Django's built-in LoginView and LogoutView for efficient session management.

Profile Management – Authenticated users can view and update their profile via a custom UserUpdateForm and a protected profile view.

Blog Post Management Features 📝
This section of the project implements full CRUD functionality for blog posts, using Django's powerful class-based views.

Post Model – A custom model to store post data, including title, content, author, and published_date.

Create Posts – A CreateView allows logged-in users to create new blog posts.

View Posts – Posts are displayed on the home page using a ListView, and individual posts can be viewed in detail using a DetailView.

Update & Delete Posts – The UpdateView and DeleteView allow a post's author to edit or remove their own content. These views are protected using LoginRequiredMixin and UserPassesTestMixin to enforce ownership.

Code Structure
blog/models.py
Post – The model for a blog post. Includes a ForeignKey to the User model and a get_absolute_url method for redirection.

UserRegistrationForm – Custom form for handling user sign-up.

UserUpdateForm – ModelForm for updating an authenticated user's username and email.

blog/views.py
register – Handles new user registration.

profile – Protected by @login_required, allows authenticated users to view and edit their profile.

PostListView – Displays a list of all blog posts on the home page.

PostDetailView – Displays a single blog post's content.

PostCreateView – Renders a form for creating a new post. Protected by LoginRequiredMixin.

PostUpdateView – Renders a form for updating an existing post. Protected by LoginRequiredMixin and UserPassesTestMixin.

PostDeleteView – Handles the deletion of a post. Protected by LoginRequiredMixin and UserPassesTestMixin.

blog/urls.py
/register/ → register view

/login/ → Django's LoginView

/logout/ → Django's LogoutView

/profile/ → profile view

/ → PostListView

/post/<int:pk>/ → PostDetailView

/post/new/ → PostCreateView

/post/<int:pk>/update/ → PostUpdateView

/post/<int:pk>/delete/ → PostDeleteView

blog/templates/blog/
register.html – Registration page

login.html – Login page

logout.html – Logout confirmation page

profile.html – Profile view and edit page

home.html – Main blog page displaying all posts

post_detail.html – Individual post detail page

post_form.html – Template for creating and updating posts

post_confirm_delete.html – Confirmation page for deleting a post

Testing Instructions
Test Authentication System
Run the Server

Bash

python manage.py runserver
Test Registration: Visit http://127.0.0.1:8000/blog/register/ to create a new user.

Test Login: Visit http://127.0.0.1:8000/blog/login/ to log in with valid credentials.

Test Profile Management: While logged in, visit http://127.0.0.1:8000/blog/profile/ to view and update your details.

Test Logout: Click the "Logout" link to confirm you are logged out.

Test Blog Post Management
Test Create: Log in and visit http://127.0.0.1:8000/blog/post/new/ to create a new post.

Test Read: Navigate to the home page to see all posts, then click on a post's title to view its detail page.

Test Update: While logged in as the post's author, visit the post's detail page and click the "Update" button. Edit the content and save.

Test Delete: While logged in as the post's author, click the "Delete" button on the detail page. Confirm the deletion on the next page and verify the post is removed from the home page.

Test Permissions:

Try to access the update or delete page for a post you did not author. You should be denied access.

Try to access any of the post-related management pages while logged out. You should be redirected to the login page.

Test Comment Management

Create: Log in, visit a post's detail page, fill out the comment form, and click "Post Comment." Verify the comment appears.

Update: While logged in as the comment's author, find your comment on the detail page and click "Update." Edit the content and save.

Delete: While logged in as the comment's author, find your comment on the detail page and click "Delete." Confirm the deletion on the next page.

Permissions: Try to access the update or delete URL for a comment you did not author. You should be denied access.