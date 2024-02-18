import random
import asyncio
import discord
from src.download import download

def get_token():
    with open("token.src", "r") as file:
        return file.read().strip()

async def edit_message(message_obj, response_obj, return_message):
    await response_obj.edit(content=f"<@{str(message_obj.author.id)}> {return_message}")

def run_discord_bot():
    TOKEN = get_token()

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is running.")

    @client.event
    async def on_message(message):
        global message_obj, response_obj
        if message.author == client.user:
            return
        else:
            message_obj = message

        if message.content.startswith('/yt'):          
            response_obj = await message.channel.send(f"<@{str(message.author.id)}> Downloading 0%")

            url = 0
            filebin = 'vu7lrn7ceafc' + str(random.randint(1000,9999))
            output_dir = './output'

            for word in message.content.split():
                if 'youtube.com' in word:
                    url = word
            if url == 0:
                await edit_message(message_obj, response_obj, "Couldn't find link.")
                return
            
            if '--audio-only' in str(message.content):
                link = await asyncio.create_task(download(url, output_dir, filebin, True, edit_message, message_obj, response_obj))
            else:
                link = await asyncio.create_task(download(url, output_dir, filebin, False, edit_message, message_obj, response_obj))

            await edit_message(message_obj, response_obj, f" {link}")

        # Debug
        print(f"user: '{message.author.name}' send: '{message.content}' in channel: '{message.channel}'")

    client.run(TOKEN)

run_discord_bot()
