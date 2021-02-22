import discord
import requests
import json
import random
import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
def add_encouragements(encouraging_message):
    c.execute(f'''SELECT count(*) FROM encouragements WHERE encouragement='{encouraging_message}' ''')
    if c.fetchone()[0]==0:
        c.execute(f"INSERT INTO encouragements VALUES ('{encouraging_message}')")
        conn.commit()


def get_all_encouragements():
    c.execute('''SELECT * FROM encouragements''')
    rows = c.fetchall()
    return rows

def delete_encouragements(i_will_delete_you):
    c.execute(f'''SELECT count(*) FROM encouragements WHERE encouragement='{i_will_delete_you}' ''')
    if c.fetchone()[0]!=0:
        c.execute(f"DELETE FROM encouragements WHERE encouragement='{i_will_delete_you}'")
        conn.commit()
        return 1
    return 0

client = discord.Client()

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable", "garrett"]


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

    if msg.startswith('!new'):
        encouraging_message = msg.split("!new ", 1)[1]
        add_encouragements(encouraging_message)
        await message.channel.send("A new encouraging message has been added!")

    if msg.startswith('!all'):
        rows = get_all_encouragements()
        for row in rows:
            await message.channel.send(row[0])

    if msg.startswith('!delete'):
        encouragement = msg.split("!delete ",1)[1]
        numberTest = delete_encouragements(encouragement)
        if numberTest == 1:
            await message.channel.send("An encouraging message has been deleted!")

        await message.channel.send()


    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(get_all_encouragements())[0])



client.run("Nzk5Njg0OTQ2Nzg3Njk2NjUw.YAHKpA.zYhrfjvPLBnRwedMSeJ8Ad8RrFI")