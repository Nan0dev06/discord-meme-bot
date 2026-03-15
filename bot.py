import os
import discord
import random
def get_meme():
    MEMES_FOLDER = r'C:\Users\nourh\Desktop\projects\discord_mod\memes'
    images = [f for f in os.listdir(MEMES_FOLDER) if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".webp"))]
    if not images:
        return None
    return os.path.join(MEMES_FOLDER, random.choice(images))
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$meme'):
            path = get_meme()
        if path:
            await message.channel.send(file=discord.File(path))
intents =discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token goes here') 