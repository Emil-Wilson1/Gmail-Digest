from gmail_service import authenticate, get_recent_emails


def main():

    print("Starting Gmail Digest...")

    # Authenticate with Gmail
    service = authenticate()

    print("Gmail authentication successful!")
    print()

    # Fetch recent emails
    emails = get_recent_emails(service, max_results=10)

    print(f"Found {len(emails)} emails")
    print("-" * 60)

    for email in emails:

        print(f"From: {email['from']}")
        print(f"Subject: {email['subject']}")
        print(f"Date: {email['date']}")
        print(f"Snippet: {email['snippet']}")
        print(f"Message ID: {email['id']}")
        print(f"Thread ID: {email['thread_id']}")

        print("-" * 60)


if __name__ == "__main__":
    main()