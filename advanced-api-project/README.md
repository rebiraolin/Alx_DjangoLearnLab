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

***

## Advanced Querying Capabilities

The `/api/books/` endpoint now supports filtering, searching, and ordering to provide more flexible data retrieval. These features are enabled through query parameters.

### Filtering

You can filter the list of books by specific field values.

* **`publication_year`**: Filter by a specific year.
    -   **Example**: `/api/books/?publication_year=2024`
* **`title`**: Filter by a specific title.
    -   **Example**: `/api/books/?title=The Great Adventure`

### Searching

You can perform a text search across multiple fields.

* **`search`**: Search for a keyword in the `title` or `author` fields.
    -   **Example**: `/api/books/?search=journey`

### Ordering

You can order the results by specific fields in either ascending or descending order.

* **`ordering`**: Sort by `title` or `publication_year`. Use a minus sign (`-`) for descending order.
    -   **Example (ascending)**: `/api/books/?ordering=title`
    -   **Example (descending)**: `/api/books/?ordering=-publication_year`

***

## Testing

### How to Run Tests

To run the unit tests for the API, navigate to the project's root directory and use the following command:

```bash
python manage.py test api