# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 22:39:50 2018

@author: Ryan
"""

from twilio.rest import Client

account_sid = "account sid"
auth_token = "auth token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    "PHONE_NUMBER",
    body="TESTING TESTING",
    from_="TWILIO_NUMBER"
)
