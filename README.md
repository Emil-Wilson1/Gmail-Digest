# Gmail Digest

A small open-source project for building a Gmail email digest.

The project is being developed incrementally, adding new technologies only when they are actually needed.

## Current Version

**v0.1.0 — Gmail OAuth Authentication**

### Completed

* Created Google Cloud project
* Enabled Gmail API
* Configured Google OAuth
* Created Desktop OAuth credentials
* Added development/test user
* Created Python virtual environment
* Installed Google API authentication libraries
* Implemented Gmail OAuth authentication
* Successfully authenticated with Gmail
* Generated `token.json`
* Using `gmail.readonly` scope

### Current Flow

```text
Python Application
        ↓
Google OAuth
        ↓
User Login & Permission
        ↓
Gmail Authorization
        ↓
token.json
        ↓
Authenticated Gmail API Access
```

### Project Structure

```text
Gmail-Digest/
│
├── README.md
├── .gitignore
├── main.py
├── credentials.json    # ignored
├── token.json          # ignored
└── venv/               # ignored
```

### Security

The following files must not be committed to Git:

```text
credentials.json
token.json
venv/
```

The application currently requests:

```text
https://www.googleapis.com/auth/gmail.readonly
```

This provides read-only access to Gmail.

## Next

Use the authenticated Gmail API connection to retrieve actual emails.
