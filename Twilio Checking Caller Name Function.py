# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 21:37:27 2018

@author: Ryan
"""




from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = "account sid"
auth_token = "account token"
client = Client(account_sid, auth_token)

number_to_lookup = "+16307889299" 

def number_lookup(number_to_lookup):
    name = client.lookups.phone_numbers(number_to_lookup).fetch(type='caller-name')
    print((name.caller_name)['caller_name'])
    
number_lookup(number_to_lookup)
