import csv
import os
from dotenv import load_dotenv
from generate_email import generate_email
from send_email import send_email
import pyfiglet

# ASCII Banner
banner = pyfiglet.figlet_format("K S Nitin", font="slant")
print(banner)
print("Welcome to the Email Automation Script!")
# Load environment variables
load_dotenv()

# CONFIG
csv_path = os.getenv("CSV_PATH")
resume_path = os.getenv("RESUME_PATH")
subject = os.getenv("SUBJECT")
email_user = os.getenv("EMAIL_ADDRESS")
email_pass = os.getenv("EMAIL_PASSWORD")

# Main Logic
with open(csv_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row["Name"]
        to_email = row["Email"]
        company = row["Company"]

        body = generate_email(name, company)
        send_email(
            to_email,
            subject,
            body,
            resume_path,
            email_user,
            email_pass
        )