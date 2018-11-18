from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "ACf364e45e95cd0748f3705405e7e50b34"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "eb04e4621419cf313010053f79106a42"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello phone's @velacosi",
    to="+5511999696172", 
    from_="+552139579039")

print message.sid
