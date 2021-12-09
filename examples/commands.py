import discord
from discord.ext import commands

# бот для команд, выданы все намерения
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_ready
@bot.event
async def on_ready():
	print(f'{bot.user} запущен и готов к работе!')

# подробнее про это событие: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_messagemessage
@bot.event
async def on_message(message):
	# если сообщение от бота - игнорируем
	if message.author.bot:
		return
	# проверяем, является ли сообщение командой
	await bot.process_commands(message)

"""
подробнее про команды: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4
"""

@bot.command(aliases=['test', 'тест', 'тестовая_команда', 'test_command'])
async def test_(ctx):
	# список свойств и методов контекста можно найти в документации по запросу context
	await ctx.send('Успешный тест!')

@bot.command()
async def get_values(ctx, number: int, boolean: bool, member: discord.Member):
	print(f'number = {number}, type = {type(number)}')
	print(f'boolean = {boolean}, type = {type(boolean)}')
	print(f'member = {member}, type = {type(member)}')

@bot.command()
async def get_text(ctx, first_word, second_word, *, other_text):
	print(f'Первое слово: {first_word}, длина: {len(first_word)}')
	print(f'Второе слово: {second_word}, длина: {len(second_word)}')
	print(f'Остальной текст: {other_text}, длина: {len(other_text)}')

# запускаем бота
bot.run('TOKEN')
