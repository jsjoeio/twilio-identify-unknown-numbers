from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
import os

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

def sendMessage(message):
  message = client.messages \
    .create(
          body=message,
          from_=os.getenv("TWILIO_NUMBER"),
          to=os.getenv("PHONE_NUMBER")
                  )