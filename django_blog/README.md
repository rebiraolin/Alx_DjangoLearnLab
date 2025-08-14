# Django Blog Project – Authentication, Post Management, Tagging, and Search

This repository contains the code for a Django blog project, developed as part of the **ALX_DjangoLearnLab** curriculum.  
The project implements a **secure authentication system**, **full blog post CRUD functionality**, a **tagging feature**, and a **search engine**.

---

## 🚀 Features

### **1. Authentication System**
Built using Django's built-in authentication tools with custom forms and views for an enhanced user experience.

- **User Registration** – Extended Django's default `UserCreationForm` to include an email field.
- **Login & Logout** – Managed by Django's `LoginView` and `LogoutView`.
- **Profile Management** – Authenticated users can view and update their username and email.

---

### **2. Blog Post Management 📝**
Full CRUD functionality for blog posts using Django's class-based views.

- **Post Model** – Stores title, content, author, and published date.
- **Create Posts** – Available to logged-in users.
- **Read Posts** – Posts listed on the home page, with individual detail views.
- **Update & Delete** – Only the post's author can edit or delete their posts.

---

### **3. Tagging System**
Implemented with [`django-taggit`](https://django-taggit.readthedocs.io/).

- Add multiple tags to a post using a comma-separated list.
- Tags appear as clickable links on post detail pages.
- Clicking a tag shows all posts with that tag.

---

### **4. Search Engine 🔎**
A search bar on every page allows keyword searches.

- Searches post **title**, **content**, and **tags**.
- Displays relevant results in a dedicated search results page.

---

## 📂 Code Structure

blog/
│
├── models.py
│ └── Post – Blog post model with TaggableManager for tags.
│
├── forms.py
│ └── UserRegistrationForm – Custom user sign-up form.
│ └── UserUpdateForm – Form for updating username and email.
│ └── PostForm – Includes title, content, and tags.
│
├── views.py
│ └── register – Handles new user registration.
│ └── profile – View and edit user profile.
│ └── PostListView – Displays all blog posts.
│ └── PostDetailView – Displays post content with tags.
│ └── PostCreateView – Create a new post.
│ └── PostUpdateView – Update an existing post.
│ └── PostDeleteView – Delete a post.
│ └── PostListByTagView – List posts by a specific tag.
│ └── PostSearchView – Search posts by keyword.
│
├── urls.py
│ ├── /register/
│ ├── /login/
│ ├── /logout/
│ ├── /profile/
│ ├── / – PostListView
│ ├── /post/int:pk/ – PostDetailView
│ ├── /post/new/ – PostCreateView
│ ├── /post/int:pk/update/ – PostUpdateView
│ ├── /post/int:pk/delete/ – PostDeleteView
│ ├── /tags/slug:tag_slug/ – PostListByTagView
│ ├── /post/search/ – PostSearchView
│
└── templates/blog/
├── base.html – Includes search bar in navigation.
├── register.html – Registration form.
├── login.html – Login form.
├── logout.html – Logout confirmation.
├── profile.html – Profile view/edit.
├── home.html – Post list.
├── post_detail.html – Post detail with tags.
├── post_form.html – Create/update form.
├── post_confirm_delete.html – Delete confirmation.
├── post_search.html – Search results.
├── post_list_by_tag.html – Posts by tag.

yaml
Copy code

---

## 🧪 Testing Instructions

### **Authentication**
1. **Run the server**  
   ```bash
   python manage.py runserver
Register – Visit:
http://127.0.0.1:8000/blog/register/

Login – Visit:
http://127.0.0.1:8000/blog/login/

Profile Update – While logged in, visit:
http://127.0.0.1:8000/blog/profile/

Logout – Click "Logout" in the navigation bar.

Post Management
Create – http://127.0.0.1:8000/blog/post/new/

Read – View posts on the home page.

Update – Only post authors can update their posts.

Delete – Only post authors can delete their posts.

Permissions – Non-authors cannot edit/delete other users’ posts.

Tagging
Create a post with tags: django, python, webdev.

On the post detail page, click a tag to see related posts.

Search
Use the search bar in the navigation.

Try searching by:

A word in the title

A word in the content

A tag

All searches return relevant posts.

🛠️ Tech Stack
Backend: Django 5.x

Database: SQLite (default; can be switched to PostgreSQL/MySQL)

Tagging: django-taggit

Frontend: Django templates (HTML/CSS)

