import discord 
import os
import requests
import json
from replit import db
from time import sleep



client = discord.Client()

def get_data():
  response = requests.get('https://api.mcsrvstat.us/2/Weloveminecraft22.aternos.me')
  json_data = json.loads(response.text)
  data = json_data["online"]
  return(data)

def urmom():
  momjoke = requests.get('https://api.yomomma.info/')
  json_data = json.loads(momjoke.text)
  joke = json_data["joke"]
  return(joke)

@client.event
async def on_ready():
  print("Ready")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  if msg.startswith("!darkjoke"):
      res = requests.get('https://v2.jokeapi.dev/joke/Dark')
      js = json.loads(res.text)
      quest = js["setup"]
      pun = js["delivery"]

      await message.channel.send(quest)
      sleep(3)
      await message.channel.send(pun)

  if msg.startswith("!status"):
    stat = get_data()
    if stat == True:
      await message.channel.send("The server is online")
    elif stat == False:
      await message.channel.send("The server is offline")
    else:
      await message.channel.send("Unknown status")

  if msg.startswith("!yourdad"):
    await message.channel.send("My creator is Nordic Games aka Lukas")

  if msg.startswith("!momjoke"):
    jk = urmom()
    await message.channel.send(jk)

client.run(os.getenv("TOKEN"))

git init
