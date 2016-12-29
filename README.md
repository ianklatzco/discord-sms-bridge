# Discord-SMS bridge

sends discord server messages to a phone via sms.

connects a single number with an **entire** discord server.

for my friend with windows phone and without regular computer access.

can be easily modified to just a single channel.

* requires a verified account (ie, add a credit card) in heroku
* and a non-trial account (ie, put $20 in and buy a $1/mo phone #) in twilio

**DON'T make this a public repo or fork it publicly.**
your twilio and discord secret keys will be publicly exposed (bad)

store them in shell environment variables or use a private repo or don't push this to a public github repo.

## usage

* create discord app, make it into a bot, get discord bot token and client ID
* add discord bot to a server you have permissions to via https://discordapp.com/oauth2/authorize?client_id=BOTCLIENTID&scope=bot&permissions=0
* create twilio account, get a number and twilio account sid and auth token
* put these tokens in the corresponding fields in bot.py and webserver.py.
* fill out the rest of the variables in these two files (phone number, bot name, url)
* set up heroku account, install heroku-toolbelt, heroku login
* set up heroku app ```heroku create discord-sms -s cedar``` from inside this repo
* set sms url in twilio settings to point to heroku app url (```heroku open```)
* finally, ```heroku ps:scale web=1 worker=1```

debug problems w ```heroku logs```

or shoot me a message on twitter. feedback's appreciated!

thanks to zoe helding for her help.
