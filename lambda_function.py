from __future__ import print_function
from helpers import *

def lambda_handler(event, context):
    # Obtain the number from the incoming text
    number = parse_number(event['Body'])
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

    to_number = event['From']
    # Since the to_number is not formatted corrected, we add a + and slice off the first three chars and add a +
    # For example, the number looks like %2B16025551234, so we slice off %2B and add a plus.
    send_message(message, '+' + to_number[3:])

    print("Received event: " + str(event))
    return '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'\
           '<Response><Message>Hello world! -Lambda</Message></Response>'