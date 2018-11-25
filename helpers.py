from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
import os

# Your Account Sid and Auth Token from twilio.com/console
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)

def lookup_number(number_to_lookup):
  """
  This function accepts a number (expected format +1XXXXXXXXXX) and returns the callers name.
  """
  name = client.lookups.phone_numbers(number_to_lookup).fetch(type='caller-name')
  if name:
    return (name.caller_name)['caller_name']
  else:
    return False


def send_message(message, to_number):
  """
  This function accepts as message (String), and then runs the function to send a text
  using Twilio's SMS API.
  """
  message = client.messages \
    .create(
          body=message,
          from_=os.getenv("TWILIO_NUMBER"),
          to=to_number
                  )

def parse_number(message):
  """
  This function accepts a message (String), which has a phone number inside.
  If it finds a phone number, it parses it then returns the phone number.
  """
  import re
  # Check for at least two numbers
  if bool(re.search(r'\d{2}', message)):
    # Clean up number
    cleanedUpNumber = re.sub(r'([-() ])', "", message)
    # Check if it's less than 10 digits
    if len(cleanedUpNumber) < 10:
      return False
    elif len(cleanedUpNumber) == 10:
      return '+1' + cleanedUpNumber
    elif len(cleanedUpNumber) > 10:
      # Check for countryCode
      countryCode = '+1'
      if (cleanedUpNumber[0:2] == countryCode):
        return cleanedUpNumber
    else:
      return False
  else:
    return False