# Advanced API Development with Django REST Framework

This project is an advanced API for managing a library of authors and books. It uses Django REST Framework to create a robust and efficient API with advanced querying capabilities.

## API Endpoints

### List Books
- **URL**: `/api/books/`
- **Method**: `GET`
- **Permissions**: `AllowAny` (public access)
- **Description**: Retrieves a list of all books in the database.

### Create Book
- **URL**: `/api/books/create/`
- **Method**: `POST`
- **Permissions**: `IsAuthenticated` (authenticated users only)
- **Description**: Creates a new book instance. Requires authentication.

### Retrieve Book Details
- **URL**: `/api/books/<int:pk>/detail/`
- **Method**: `GET`
- **Permissions**: `AllowAny` (public access)
- **Description**: Retrieves the details of a single book by its primary key.

### Update Book
- **URL**: `/api/books/<int:pk>/update/`
- **Methods**: `PUT`, `PATCH`
- **Permissions**: `IsAuthenticated` (authenticated users only)
- **Description**: Updates an existing book instance. `PUT` requires all fields; `PATCH` can update a subset of fields.

### Delete Book
- **URL**: `/api/books/<int:pk>/delete/`
- **Method**: `DELETE`
- **Permissions**: `IsAuthenticated` (authenticated users only)
- **Description**: Deletes a book instance from the database.