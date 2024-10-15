# Made by Elijah Sarver, 2022
import tkinter as t
from discord import Webhook, SyncWebhook, colour
import discord


#Code for discord WebHook

#insert your discord webhook url

url = ''


hook = SyncWebhook.from_url(url)



# Main Window
win = t.Tk()
win.configure(bg='gray')
win.title("Discord Message Sender for Web Hook")
win.geometry('400x100')

# Label that tells user what the text entry box does
l1 = t.Label(text="what do you want the webhook to send",
fg='black',
bg='gray')

l1.pack()

# Text Entry Box
e1 = t.Entry(width=80,
bg="darkgray")

e1.pack()

   
#sends the request
def carrot():
    hook.send(e1.get())

# Button to call webhook request
b1 = t.Button(
    text="Send it",
    width=15,
    height=5,
    bg="gray",
    command=carrot
)


b1.pack()

t.mainloop()
