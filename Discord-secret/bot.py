import discord
import random
from discord.ext import commands

TOKEN = 'Nzc1MzgxMjEyNjgzNjk4MTc3.X6lgBg.pWhC8DVF-j6bnD7Q5HEz_Csf_7o'

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('coding!'))
	print('Bot is ready')


@client.command(name='hello', help='This command returns a random hello message')
async def hello(ctx):
	responses = ['***grumble*** Why did you wake me op?!', 'Top of the morning you lad!']
	await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words!')
async def die(ctx):
	responses = ['Why have you brought my short life to an end?', 'I could have done so much more!', 'I have a family! Kill them instead of me!']
	await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits.')
async def credits(ctx):
	await ctx.send('Made by Simonkey.')
	await ctx.send('Thanks to Simonkey to bringing up the idea.')
	await ctx.send('Thanks to you all for giving me the command ideas!')


@client.command()
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	member_name, member_discriminator = member.split('#')

	for ban_entry in banned_users:
		user = ban_entry.user 

		if (user.name, user.discriminator) == (member_name, member_discriminator):	
			await ctx.guild.unban(user)
			await ctx.send(f'Unbanned {user.name}#{user.discriminator}')
			return

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
	await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
	await member.ban(reason=reason)	


@client.command()
async def clear(ctx, amount:int = 10):
	await ctx.channel.purge(limit=amount)

	
@client.command()
async def ping(ctx):
	await ctx.send(f'Pong!{round(client.latency *1000)}ms')

@client.command(name='8ball', help='Ask a question! The bot will respond on it!')
async def _8ball(ctx, *, question):
	responses = ['No, never gonna happen!',
			     'For sure!',
			     'I dont know.']
	await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def on_member_join(member):
	channel = discord.utils.get(member.guild.channels, name='welcome')
	print(f'{user.name} just joined the server! Hope he will have a nice time around here!')

@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, name='welcome')
	print(f'{user.name} just left the server... hope we will see him very soon!')

client.run(TOKEN)