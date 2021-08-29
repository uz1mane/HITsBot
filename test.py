import discord
from discord import utils
from discord.ext import commands

import config

intents = discord.Intents.all()

class MyClient(discord.Client):
	async def on_ready(self):
		print ('Logged an as {0}!'.format(self.user))

	#newly joined user gets guest role
	# async def on_member_join(member):
	#     role = discord.utils.get(member.guild.roles, id=config.AUTO_ROLE_ID)
	#     await member.add_roles(role)
	#     print("{} joined to channel! Role: {}".format(member, role.id))


#for grades
	async def on_raw_reaction_add(self, payload):
		if (payload.message_id == config.GRADES_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try:
				emoji = str(payload.emoji.name)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])

				if (len([i for i in member.roles if i.id not in config.EXCROLES_FOR_GRADES]) <= config.MAX_ROLES_PER_USER):
					await member.add_roles(role)
					print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))		
				else:
					await message.remove_reaction(payload.emoji, member)
					print('[ERROR] Too many roles for user {0.display_name}'.format(member, role))	

			except KeyError as e:
				print('[ERROR] Key Error, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

		if (payload.message_id == config.INTERESTS_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try:
				emoji = str(payload.emoji.name)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])

				await member.add_roles(role)
				print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))										

			except KeyError as e:
				print('[ERROR] Key Error, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

		if (payload.message_id == config.GROUP_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try:
				emoji = str(payload.emoji.name)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])

				if (len([i for i in member.roles if i.id not in config.EXCROLES_FOR_GROUPS]) <= config.MAX_ROLES_PER_USER):
					await member.add_roles(role)
					print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))		
				else:
					await message.remove_reaction(payload.emoji, member)
					print('[ERROR] Too many roles for user {0.display_name}'.format(member, role))	

			except KeyError as e:
				print('[ERROR] Key Error, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

	async def on_raw_reaction_remove(self, payload):
		if (payload.message_id == config.GRADES_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try: 
				emoji = str(payload.emoji)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])
			
				await member.remove_roles(role)
				print('[SUCCESS] Role {1.name} has been removed from user {0.display_name} '.format(member, role))		
			
			except KeyError as e:
				print('[ERROR] KeyError, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

		if (payload.message_id == config.INTERESTS_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try: 
				emoji = str(payload.emoji)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])
			
				await member.remove_roles(role)
				print('[SUCCESS] Role {1.name} has been removed from user {0.display_name} '.format(member, role))		
			
			except KeyError as e:
				print('[ERROR] KeyError, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

		if (payload.message_id == config.GROUP_POST_ID):
			channel = self.get_channel(payload.channel_id) 
			message = await channel.fetch_message(payload.message_id)
			member = utils.get(message.guild.members, id=payload.user_id)

			try: 
				emoji = str(payload.emoji)
				role = utils.get(message.guild.roles, id=config.ROLES[emoji])
			
				await member.remove_roles(role)
				print('[SUCCESS] Role {1.name} has been removed from user {0.display_name} '.format(member, role))		
			
			except KeyError as e:
				print('[ERROR] KeyError, no role found for ' + emoji)
			except Exception as e:
				print(repr(e))

#for interests
	# async def on_raw_reaction_add(self, payload):
	# 	if (payload.message_id == config.INTERESTS_POST_ID):
	# 		channel = self.get_channel(payload.channel_id) 
	# 		message = await channel.fetch_message(payload.message_id)
	# 		member = utils.get(message.guild.members, id=payload.user_id)

	# 		try:
	# 			emoji = str(payload.emoji.name)
	# 			role = utils.get(message.guild.roles, id=config.ROLES[emoji])

	# 			if (len([i for i in member.roles if i.id not in config.EXCROLES]) <= 5):
	# 				await member.add_roles(role)
	# 				print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))		
	# 			else:
	# 				await message.remove_reaction(payload.emoji, member)
	# 				print('[ERROR] Too many roles for user {0.display_name}'.format(member, role))	

	# 		except KeyError as e:
	# 			print('[ERROR] Key Error, no role found for ' + emoji)
	# 		except Exception as e:
	# 			print(repr(e))

	# async def on_raw_reaction_remove(self, payload):
	# 	if (payload.message_id == config.INTERESTS_POST_ID):
	# 		channel = self.get_channel(payload.channel_id) 
	# 		message = await channel.fetch_message(payload.message_id)
	# 		member = utils.get(message.guild.members, id=payload.user_id)

	# 		try: 
	# 			emoji = str(payload.emoji)
	# 			role = utils.get(message.guild.roles, id=config.ROLES[emoji])
			
	# 			await member.remove_roles(role)
	# 			print('[SUCCESS] Role {1.name} has been removed from user {0.display_name} '.format(member, role))		
			
	# 		except KeyError as e:
	# 			print('[ERROR] KeyError, no role found for ' + emoji)
	# 		except Exception as e:
	# 			print(repr(e))

	# async def on_message(self, message):
	# 	print ('Message from {0.author}: {0.content}'.format(message))

client = discord.Client(intents=intents)
client = MyClient(intents=intents)
client.run(config.TOKEN)


