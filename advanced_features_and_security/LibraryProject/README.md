# Advanced Features and Security (Django Project)

This project focuses on implementing advanced features and security best practices in a Django application.

## Security Measures Implemented (Task 2)

This section details the security enhancements applied to the application to protect against common web vulnerabilities.

### 1. Secure Settings Configuration
Django's `settings.py` has been configured with the following:
- `DEBUG = False` (Note: Currently `True` for development, but must be `False` in production)
- `SECURE_CONTENT_TYPE_NOSNIFF = True`: Prevents browsers from MIME-sniffing.
- `SECURE_BROWSER_XSS_FILTER = True`: Enables browser's built-in XSS protection.
- `X_FRAME_OPTIONS = 'DENY'`: Protects against clickjacking by preventing embedding the site in iframes.
- `SESSION_COOKIE_SECURE = True`: Ensures session cookies are only sent over HTTPS.
- `CSRF_COOKIE_SECURE = True`: Ensures CSRF tokens are only sent over HTTPS.

### 2. CSRF Protection for Forms
All forms handling `POST` requests include `{% csrf_token %}` to prevent Cross-Site Request Forgery (CSRF) attacks. This is specifically implemented in:
- `bookshelf/templates/bookshelf/book_form.html`
- `bookshelf/templates/bookshelf/book_form_edit.html`

### 3. Secure Data Access in Views
Data input and database interactions are secured by:
- **Using Django's ORM:** All database queries (e.g., `Book.objects.all()`, `form.save()`) leverage Django's ORM, which automatically parameterizes queries, preventing SQL Injection.
- **Django Forms for Validation & Sanitization:** User inputs for creating/editing books are handled via `bookshelf/forms.py` (`BookForm`). Django Forms ensure data validation (e.g., correct data types) and sanitization before data is processed or saved to the database. This mitigates risks like XSS via stored data.
(See `bookshelf/views.py` `book_create_view` and `bookshelf/forms.py`)

### 4. Content Security Policy (CSP) Implementation
A Content Security Policy has been configured using `django-csp` middleware to reduce the risk of XSS attacks.
- **Middleware:** `csp.middleware.CSPMiddleware` is active.
- **Directives:**
    ```python
    CONTENT_SECURITY_POLICY = {
        'DIRECTIVES': {
            'default-src': ("'self'",),
            'script-src': ("'self'",),
            'style-src': ("'self'",),
            'img-src': ("'self'",),
            'font-src': ("'self'",),
            'connect-src': ("'self'",),
            'base-uri': ("'self'",),
            'object-src': ("'none'",),
            'frame-ancestors': ("'self'",),
        }
    }
    ```
These directives restrict content loading to trusted sources (primarily 'self'), blocking malicious injections.

### 5. Basic Testing Conducted
- **CSRF:** Verified presence of `csrfmiddlewaretoken` in form source code.
- **SQL Injection:** Confirmed data saving via Django ORM with valid/invalid inputs.
- **XSS:** Implicitly mitigated by Django Forms/ORM and explicitly by CSP.
- **CSP Header:** Verified `Content-Security-Policy` header presence in browser network tools.


## Task 3: Implementing HTTPS and Secure Redirects (Deployment Configuration)

For production deployment, ensuring HTTPS is served correctly involves configuring a web server (e.g., Nginx or Apache) to handle SSL/TLS termination and certificate management. Django's `SECURE_SSL_REDIRECT` and HSTS settings rely on the web server correctly identifying HTTPS traffic.

### SSL/TLS Certificates

* **Acquisition:** Obtain SSL/TLS certificates from a Certificate Authority (CA) such as Let's Encrypt (free, automated via Certbot), Comodo, DigiCert, etc. For Let's Encrypt, the `certbot` tool is widely used to automate certificate issuance and renewal.
* **Location:** Store certificates (e.g., `fullchain.pem` and `privkey.pem`) securely on the server.

### Web Server Configuration (Example: Nginx)

Below is a conceptual Nginx server block configuration. This would typically be placed in a file like `/etc/nginx/sites-available/your_domain.conf` and then symlinked to `/etc/nginx/sites-enabled/`.

```nginx
# Redirect HTTP to HTTPS
server {
    listen 80;
    listen [::]:80;
    server_name your_domain.com www.your_domain.com; # Replace with your actual domain

    return 301 https://$host$request_uri;
}

# HTTPS Server Block
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name your_domain.com www.your_domain.com; # Replace with your actual domain

    ssl_certificate /etc/letsencrypt/live/your_[domain.com/fullchain.pem](https://domain.com/fullchain.pem); # Path to fullchain certificate
    ssl_certificate_key /etc/letsencrypt/live/your_[domain.com/privkey.pem](https://domain.com/privkey.pem); # Path to private key
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;
    ssl_protocols TLSv1.2 TLSv1.3; # Enforce strong protocols
    ssl_prefer_server_ciphers on;
    ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH"; # Strong ciphers
    ssl_stapling on;
    ssl_stapling_verify on;
    resolver 8.8.8.8 8.8.4.4 valid=300s; # Google Public DNS
    resolver_timeout 5s;

    # HSTS Header (set by Django's SECURE_HSTS_SECONDS, but can also be set here)
    # add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    # Root directory for your static and media files
    root /path/to/your/project/staticfiles; # Update this path

    # Serve static files directly
    location /static/ {
        alias /path/to/your/project/staticfiles/; # Update this path
    }

    # Serve media files (if applicable)
    location /media/ {
        alias /path/to/your/project/mediafiles/; # Update this path
    }

    # Proxy requests to Gunicorn/uWSGI (your Django application server)
    location / {
        proxy_pass http://unix:/path/to/your/gunicorn.sock; # Or [http://127.0.0.1:8000](http://127.0.0.1:8000);
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme; # Crucial for Django's SECURE_SSL_REDIRECT
        proxy_redirect off;
    }
}

## Security Review (Task 3)

This section summarizes the comprehensive security measures implemented across Task 2 and Task 3, outlining their contribution to the application's overall security posture.

### Contribution to Security:

1.  **Fundamental Django Security Defaults:** The project leverages Django's built-in security features, including its robust ORM to prevent SQL injection, secure session management, and password hashing for user authentication.
2.  **Secure Settings Configuration:** Critical settings like `SECURE_CONTENT_TYPE_NOSNIFF`, `SECURE_BROWSER_XSS_FILTER`, `X_FRAME_OPTIONS = 'DENY'`, `SESSION_COOKIE_SECURE = True`, and `CSRF_COOKIE_SECURE = True` have been enabled. These directly combat vulnerabilities such as MIME-sniffing, XSS, clickjacking, and ensure sensitive cookies are only transmitted over secure connections.
3.  **Cross-Site Request Forgery (CSRF) Protection:** The use of `{% csrf_token %}` in all forms requiring `POST` requests effectively prevents CSRF attacks by ensuring that form submissions originate from the legitimate site.
4.  **Secure Data Access and Input Validation:** By employing Django's `ModelForms`, all user input is automatically validated and sanitized, significantly reducing the risk of stored XSS, malicious data injection, and other data integrity issues. The ORM ensures all database interactions are parameterized.
5.  **Content Security Policy (CSP):** The integration of `django-csp` with strict `default-src 'self'` and other directives acts as a strong defense against Cross-Site Scripting (XSS) attacks, limiting the sources from which content can be loaded.
6.  **HTTPS Enforcement and HSTS:**
    * `SECURE_SSL_REDIRECT = True` ensures all HTTP traffic is automatically upgraded to HTTPS, preventing downgrade attacks.
    * `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, and `SECURE_HSTS_PRELOAD` implement HTTP Strict Transport Security (HSTS). This header instructs browsers to *only* communicate with the site over HTTPS for a defined period, even for subsequent visits or when a user types `http://`. This significantly enhances protection against passive eavesdropping and certain active attacks.
7.  **Deployment Configuration for HTTPS:** While implemented conceptually for this development environment, the documentation for Nginx configuration (or similar web server) highlights the crucial role of external web servers in handling SSL/TLS termination, certificate management, and correctly passing `X-Forwarded-Proto` to Django for full HTTPS enforcement in production.

### Potential Areas for Improvement:

1.  **Logging and Monitoring:** Implement comprehensive logging for security events (e.g., failed logins, permission denials, CSP violations) and integrate with a monitoring system.
2.  **Rate Limiting:** Implement rate limiting for authentication endpoints (login, password reset) to mitigate brute-force and denial-of-service attacks.
3.  **Two-Factor Authentication (2FA):** For higher security requirements, implement 2FA for user accounts.
4.  **Security Scanning and Audits:** Regularly use automated security scanners and conduct manual security audits (penetration testing) to identify new vulnerabilities.
5.  **Sensitive Data Handling:** Ensure any sensitive user data beyond what's currently handled (e.g., payment info) is encrypted at rest and in transit, and follows strict data retention policies.
6.  **Error Handling:** Implement custom, generic error pages to avoid leaking sensitive information through Django's default debug error pages in production. (Ensure `DEBUG=False` in production).