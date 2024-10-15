# Elijah Sarver 2022-2024
from discord import Webhook, SyncWebhook

#slightly less anoying bastard by elijah sarver

#insert your discord webhook url

url = ''

#webhook will send this message
texttoyell = input("What do you want it to say: ")

#cool fun webhook
 
urlweb = SyncWebhook.from_url(url)

urlweb.send(texttoyell)
