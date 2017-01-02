# whenever an sms is received by twilio,
# twilio makes a post request @ url specified in twilio settings,
# then send the message to discord.
from flask import Flask, request, redirect
import twilio.twiml
import requests
import json

channelID = XXXXXXXXXXXXXXXXXX # channel to send texts to. enable dev mode on discord and right-click on the channel: "Copy ID"
botToken  = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
botName   = "sms-bot" # doesn't have to be the real bot name, just for user-agent
yourUrl   = "http://some.url" # idk what this is supposed to be. it's for user agent.
#                               not important

###############################################################################
baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"{} ({}, v0.1)".format(botName,yourUrl),
            "Content-Type":"application/json", }

app = Flask(__name__)

"""POSTs incoming texts to discord server"""
@app.route("/", methods=['GET', 'POST'])
def main():
    message = request.values.get("Body",None)
    POSTedJSON =  json.dumps ( {"content":message} )
    r = requests.post(baseURL, headers = headers, data = POSTedJSON)

    resp = twilio.twiml.Response()
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)