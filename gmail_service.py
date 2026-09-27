import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def authenticate():
    creds = None

    # Load previously saved credentials
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    # Refresh expired credentials
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())

    # First-time authentication
    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )

        creds = flow.run_local_server(port=0)

        # Save credentials for future runs
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build("gmail", "v1", credentials=creds)


def get_recent_emails(service, max_results=10):

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for message in messages:

        message_data = service.users().messages().get(
            userId="me",
            id=message["id"],
            format="metadata",
            metadataHeaders=[
                "From",
                "Subject",
                "Date"
            ]
        ).execute()

        headers = message_data["payload"]["headers"]

        email = {
            "id": message_data["id"],
            "thread_id": message_data["threadId"],
            "snippet": message_data.get("snippet", ""),
            "from": "",
            "subject": "",
            "date": ""
        }

        for header in headers:

            if header["name"] == "From":
                email["from"] = header["value"]

            elif header["name"] == "Subject":
                email["subject"] = header["value"]

            elif header["name"] == "Date":
                email["date"] = header["value"]

        emails.append(email)

    return emails