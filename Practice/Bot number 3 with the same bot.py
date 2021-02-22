import discord
import requests
import json
import random
import sqlite3

conn = sqlite3.connect('example.db')
c = conn.cursor()

c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')

c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

conn.commit()
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())
conn.close()

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "garrett"]
starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!",
    "Eat some yogurt!"
]

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run("Nzk5Njg0OTQ2Nzg3Njk2NjUw.YAHKpA.zYhrfjvPLBnRwedMSeJ8Ad8RrFI")