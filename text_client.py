from secrets import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, CELL_NUMBER

from twilio.rest import Client

# authorization set up

account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

# this sends a text message to the number
# ! could be used in addition to DM functionality?
message = client.messages.create(
    to=CELL_NUMBER, from_="+12059272325", body="i am a bot"
)

print(message.sid)

