# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from decouple import config

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

account_sid = config('ACCOUNT_SID')
auth_token = config('AUTH_TOKEN')
client = Client(account_sid, auth_token)


def send_sms(message, phoneNumbers=[]):
    if len(phoneNumbers) < 1:
        print("No phone numbers added")
    # Temp to prevent sending too many message
    elif len(phoneNumbers) > 10:
        print("Trying to send too many messages")
    else:
        try:
            for number in phoneNumbers:
                message = client.messages \
                    .create(
                        body=message,
                        from_='+13603835176',
                        to=number
                    )
                print("Message sent to: " + number)
        except TwilioRestException:
            print("Error with Twilio")
