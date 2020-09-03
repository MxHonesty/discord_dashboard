import discord
from threading import Thread
from secret import TOKEN

client = discord.Client()

def start_bot():
    if __name__ == '__main__':      # cand ruleaza botul in mod standalone
        print('Se conecteza la discord DIN MAIN')
    else:                           # cand ruleaza botul in modul webserver
        print('Se conecteaza la discord...')

    client.run(TOKEN)

# Run the bot on its own thread
thread = Thread(target=start_bot, args=())
thread.start()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:   #nu isi raspunde singur
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
