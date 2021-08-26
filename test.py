import discord
from discord import utils

import config

class MyClient(discord.Client):
	async def on_ready(self):
		print ('Logged an as {0}!'.format(self.user))

	async def on_message(self, message):
		print ('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(config.TOKEN)



