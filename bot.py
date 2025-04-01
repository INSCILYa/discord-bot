import discord
import random
import asyncio
import os

# Get the token from the environment variable
TOKEN = os.getenv("MTM1NjYxODI3NDA4MjkxODUyMw.GFeCGB.NATRxJitbhjrSWu1adnT0JzdNuMuupnTwG-T18")  # Make sure this environment variable is set correctly
CHANNEL_ID = 1356620660947943549

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

current_key = ""

def generate_key():
    """Generates a random key."""
    return ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=8))

async def update_key():
    """Posts a new key every hour in the Discord channel."""
    global current_key
    await client.wait_until_ready()
    
    channel = client.get_channel(1356620660947943549)
    
    while True:
        new_key = generate_key()
        current_key = new_key

        # Delete old messages (to remove previous keys)
        async for message in channel.history(limit=10):
            if message.author == client.user:
                await message.delete()
        
        # Post the new key
        await channel.send(f"🔑 **New Access Key:** `{new_key}` (Valid for 1 hour)")
        print(f"New key generated: {new_key}")

        # Wait for 1 hour before generating a new key
        await asyncio.sleep(3600)

@client.event
async def on_ready():
    print(f"Bot {client.user} is now running!")
    client.loop.create_task(update_key())

client.run(TOKEN)
