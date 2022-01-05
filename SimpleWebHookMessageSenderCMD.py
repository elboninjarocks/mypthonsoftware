from discord import Webhook, RequestsWebhookAdapter

#slightly less anoying bastard by elijah sarver

#insert your discord webhook url

url = ''

#webhook will send this message
texttoyell = input("What do you want it to say: ")

#cool fun webhook
 
urlweb = Webhook.from_url(url, adapter=RequestsWebhookAdapter())

urlweb.send(texttoyell)
