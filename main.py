import os
import discord 
import requests
import collections
import json
import random
from random import randint


SMMRY_API_KEY = os.getenv('tldr')
news_key = os.getenv('news')
tkn = os.environ['tkn']

def summry(url):
  url = "https://api.smmry.com/&SM_API_KEY="+SMMRY_API_KEY+"&SM_URL="+url
  response = requests.get(url).json()
  
  title = response['sm_api_title'] 
  body = response['sm_api_content']
  return pretty(title, body)

def pretty(title, body):
  summry = "***"+title+"***" + "\n" + "```"+body+"```"
  return summry


def news(cat):

  for i in range(15):
	  num = randint(0, 15)

  url = "https://newsapi.org/v2/top-headlines?country=us&category="+cat+"&apiKey="+news_key

  response = requests.get(url).json()

  return response['articles'][num]['url']


client = discord.Client()


@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('tldr'):
    if len(message.content) > 4:
      query = message.content[4:]
      await message.channel.send(summry(query))

  if message.content.startswith('News '):
      cat = message.content[5:]
      await message.channel.send(news(cat))
   
      
  
      
client.run(tkn)
