from __future__ import print_function
from helpers import *

def lambda_handler(event, context):
    # Obtain the number from the incoming text
    number = parse_number(event['body'])
    message = ''

    # Check for number
    if number:
      # Find out who the number belongs to
      callerName = lookup_number(number)
      if callerName:
        message = 'This number appears to be registered to: ' + callerName
      else:
        message = 'Aw. Sorry to let you down but we can\'t associate a name with that number.'
    else:
      message = 'Oops! The number you sent doesn\'t appear to be correct. Please make sure it has ten digits. Can you try sending the number again?'
    send_message(message)

    print("Received event: " + str(event))
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>Hello world! -Lambda</Message></Response>'