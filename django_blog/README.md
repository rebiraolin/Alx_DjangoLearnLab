# Django Blog Project – Authentication System

## Project Overview
This repository contains the code for a **Django blog project**, developed as part of the **Alx_DjangoLearnLab** curriculum.  
The first phase focuses on creating a secure and user-friendly **authentication system** that supports user registration, login, logout, and profile management.

## Authentication System Features
The authentication system combines Django's built-in authentication tools with custom views and forms to enhance functionality and user experience.

- **User Registration** – `UserRegistrationForm` extends Django's default user creation form to include an email field.
- **Login & Logout** – Uses Django's built-in `LoginView` and `LogoutView` for efficient session management.
- **Profile Management** – Authenticated users can view and update their profile via a custom `UserUpdateForm` and a protected profile view.

## Code Structure

### `blog/forms.py`
- **`UserRegistrationForm`** – Custom form for handling user sign-up.
- **`UserUpdateForm`** – ModelForm for updating an authenticated user's username and email.

### `blog/views.py`
- **`register`** – Handles new user registration.
- **`profile`** – Protected by `@login_required`, allows authenticated users to view and edit their profile.

### `blog/urls.py`
Authentication-related URL mappings:
- `/register/` → `register` view
- `/login/` → Django's `LoginView`
- `/logout/` → Django's `LogoutView`
- `/profile/` → `profile` view

### `blog/templates/blog/`
- `register.html` – Registration page
- `login.html` – Login page
- `logout.html` – Logout confirmation page
- `profile.html` – Profile view and edit page

## Testing Instructions
To verify the authentication system works as intended:

1. **Run the Server**
   ```bash
   python manage.py runserver

Test Registration

Visit: http://127.0.0.1:8000/blog/register/

Create a new user

Check validation errors for mismatched passwords or existing usernames

Test Login

Visit: http://127.0.0.1:8000/blog/login/

Log in with valid credentials

Ensure incorrect credentials show an error message

Test Profile Management

While logged in, visit: http://127.0.0.1:8000/blog/profile/

View and update your username and email

Confirm that logged-out users are redirected to the login page when accessing /blog/profile/

Test Logout

Click the Logout link while logged in

Confirm you are logged out and that navigation links update accordingly

pgsql
Copy
Edit
