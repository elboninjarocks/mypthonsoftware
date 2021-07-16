#All this program does is provide the user with a raw output of the html data from a website
import requests

url = input("Insert Url Containing HTML Data: ")

r = requests.get(url)

print(r.text)