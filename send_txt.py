# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC550b578456385254158c075352b0fe50"
auth_token = "ed5b6563d96147d339405fd80e8aa0b8"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="Hi Subbu !!",
    to="+12016574321",
    from_="+18623077941")
print message.sid
