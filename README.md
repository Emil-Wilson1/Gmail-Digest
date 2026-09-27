# Gmail Digest

A small open-source project for building a Gmail email digest.

The project is being developed incrementally, adding new technologies only when they are actually needed.

## Current Version

**v0.2.0 — Gmail API Email Retrieval**

### v0.1.0 — Gmail OAuth Authentication

**Completed**

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

**Flow**

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

---

## v0.2.0 — Gmail API Email Retrieval

### Goal

Use the authenticated Gmail API connection to retrieve actual emails from the user's Gmail account.

### Completed

* Reuse authenticated Gmail API connection
* Retrieve recent Gmail messages
* Retrieve individual message metadata
* Extract email sender
* Extract email subject
* Extract email date
* Extract Gmail snippet
* Extract message ID
* Extract thread ID
* Convert Gmail API responses into a simple application-friendly structure
* Display retrieved emails in the terminal

### Current Flow

```text
Python Application
        ↓
OAuth Authentication
        ↓
Authenticated Gmail API
        ↓
messages.list()
        ↓
Message IDs
        ↓
messages.get()
        ↓
Email Metadata
        ↓
┌───────────────────────┐
│ From                  │
│ Subject               │
│ Date                  │
│ Snippet               │
│ Message ID            │
│ Thread ID             │
└───────────────────────┘
        ↓
Display Emails
```

### Example Output

```text
Gmail authentication successful!

Found 10 emails
------------------------------------------------------------
From: example@gmail.com
Subject: Project Update
Date: Sat, 27 Sep 2026 10:30:00 +0530
Snippet: Here is the latest update regarding the project...
Message ID: xxxxxxxxx
Thread ID: xxxxxxxxx
------------------------------------------------------------
```

### Technologies Used

* Python
* Gmail API
* Google OAuth 2.0
* Google API Client
* Python Virtual Environment

No LLM or AI processing is being used yet.

The focus of this phase is understanding how to reliably retrieve and process Gmail data before adding AI functionality.

---

## Project Structure

```text
Gmail-Digest/

│
├── README.md
├── .gitignore
├── main.py
├── gmail_service.py
├── requirements.txt
├── credentials.json    # ignored
├── token.json          # ignored
└── venv/               # ignored
```

---

## Security

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

---

## Development Approach

The project is intentionally being developed incrementally.

Instead of introducing multiple technologies at once, each phase adds one meaningful capability.

```text
v0.1.0
OAuth Authentication
        ↓
v0.2.0
Gmail Email Retrieval
        ↓
v0.3.0
Email Parsing / Cleaning
        ↓
v0.4.0
Email Categorization
        ↓
v0.5.0
Digest Generation
        ↓
v0.6.0
LLM / AI Summarization
        ↓
Future
Automation / Scheduling / Deployment
```

The exact technologies for future phases will be introduced only when they are needed.

---

## Next

### v0.3.0 — Email Parsing & Processing

The next phase will focus on processing the retrieved Gmail data.

Planned work:

* Retrieve email bodies
* Handle plain-text emails
* Handle HTML emails
* Clean email content
* Extract useful text
* Handle attachments and unsupported content safely
* Create a consistent internal email model

After the email data is clean and structured, the project can move toward categorization and digest generation.

---

## Git History

Each version represents a small, working milestone.

Example:

```text
v0.1.0
feat: implement Gmail OAuth authentication

v0.2.0
feat: retrieve recent Gmail messages

v0.3.0
feat: parse and clean email content
```

The goal is to keep every phase understandable, testable, and independently usable.
