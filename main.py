import os
import smtplib
from email.message import EmailMessage
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

GMAIL_CREDENTIALS = {
    "user": os.environ["ADMIN_EMAIL_ADDRESS"],
    "password": os.environ["ADMIN_PASSWORD"],
}

team_details_df = pd.read_csv("./team_details.csv")
team_details = []

for index, row in team_details_df.iterrows():
    team_name = row["Team Name"]
    team_leader_email = row["Email address"]
    team_details.append({"team_name": team_name, "email": team_leader_email})

for team in team_details:
    team_name = team["team_name"]
    email = team["email"]

    msg = EmailMessage()
    msg["Subject"] = "PROJECT DETAILS SUBMISSION"
    msg["From"] = GMAIL_CREDENTIALS["user"]
    msg["To"] = email
    msg.set_content(
        f"""Hello, Leader of *{team_name}*,\n\n
Don't forget to send in your project details by tomorrow at 5 PM. Just tell me your project topic (like school management, learning management system, hotel management system etc.) and it's main features. Let's get this done smoothly.\n\nDeadline of Submission: January 11 @ 5PM\nSubmit Via (to trishan): Viber DM/Facebook DM/Reply to this mail\n\n-Trishan Mailer"""
    )

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(
        user=GMAIL_CREDENTIALS["user"], password=GMAIL_CREDENTIALS["password"]
    )
    connection.send_message(msg)
    connection.quit()
    del msg["To"]
