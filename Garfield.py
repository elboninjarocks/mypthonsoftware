#Makes A GET Request To A PNG On My Site and Writes it to Disk 
import requests

url = "https://elijahhighway.orgfree.com/3/1.png"

f = open("Garfield.png", "wb")

g = requests.get(url)


f.write(g.content)

print("Garfield Has Been Downloaded To Your Disk")

