# HTTPS Security Configuration

## Django Settings
- SECURE_SSL_REDIRECT = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

## Deployment Notes
- SSL/TLS configured via Nginx with certificate paths
- Headers mirrored in server config
- HSTS preload enabled

## Review Summary
These settings enforce HTTPS, secure cookies, and protect against XSS, clickjacking, and MIME sniffing. Recommended to test with SSL Labs and browser dev tools.
