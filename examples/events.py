import discord
from discord.ext import commands

# бот для команд, выданы все намерения
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_ready
@bot.event
async def on_ready():
	print(f'{bot.user} запущен и готов к работе!\n')

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_messagemessage
@bot.event
async def on_message(message):
	print('Поступло новое сообщение!')
	print(f'Сервер: {message.guild}')
	print(f'Канал: {message.channel}')
	print(f'Автор: {message.author}')
	print(f'ID Сообщения: {message.id}')
	print(f'Ссылка на сообщение: {message.jump_url}')
	print(f'Текст: {message.content}')

# запускаем бота
bot.run('TOKEN')
