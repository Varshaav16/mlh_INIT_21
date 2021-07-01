import discord
import os
import requests
import json 
import random
from replit import db



client = discord.Client()

sad_words = ["sad", "disappointed", "unhappy", "frustrated", "disheartened", "depressed"]

starter_encouragements = [
    "cheer up dude!",
    "Chill buddy",
    "You are really really awesome mate"
]

# if "responding"  not in db.keys():
#     db["responding"] = True

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"].value
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements

    else:
        db["encouragements"] = [encouraging_message]
        
def delete_encouragements(position):
    encouragements = db["encouragements"].value
    if len(encouragements) > position and position >= 0:
        del encouragements[position]
    db["encouragements"] = encouragements



def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "-" + json_data[0]['a']
    return quote


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content
    options = starter_encouragements
    if "encouragements" in db.keys():
        print(db["encouragements"])
        options = options + db["encouragements"].value

    

    if msg.startswith("$inspire"):
        quote = get_quote()
        await message.channel.send(quote)

    # if db["responding"]:

    if any(word in msg for word in sad_words ):
        await message.channel.send(random.choice(options)) 

    if msg.startswith("$new"):
        update_encouragements(msg.lstrip("$new "))
        await message.channel.send("Perfect! New encouraging message added")

    if msg.startswith("$del"):
        if "encouragements" in db.keys():
            delete_encouragements(int(msg.split("$del ")[1]))
        await message.channel.send("No worries deleted it, Clean! \n Check out the current list {}".format(db["encouragements"].value))
    

    if msg.startswith("$list"):
        if "encouragements" in db.keys():
            encouragements = db["encouragements"].value

        await message.channel.send(encouragements)

    # if msg.startswith("$responding"):
    #     value = msg.split("$responding ", 1)[1]

    #     if value.lower() == "true":
    #         db["responding"] = True
    #         await message.channel.send("Responding is on : )")

    #     else:
    #         db["responding"] = False
    #         await message.channel.send("Responding is off : (")
            
client.run(os.getenv('TOKEN'))



