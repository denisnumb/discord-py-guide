import discord
from discord.ext import tasks

# в данном коде не предусмотрены команды, поэтому в качестве объекта бота вполне хватит базового discord.Client
# если ваш бот подразумевает обработку команд, использовать надо более подходящий класс
# подробнее про классы ботов можно почитать здесь: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-%D0%B1%D0%BE%D1%82%D0%BE%D0%BC-%D0%B8-discord-py
bot = discord.Client(intents=discord.Intents.all())

# почитать про события (events) можно здесь: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#async-def-on_ready
@bot.event
async def on_ready():
    # запускаем задачу
    my_loop.start()
    
# почитать про задачи (tasks) можно здесь: https://github.com/denisnumb/discord-py-guide/blob/main/tasks.md
@tasks.loop(seconds=10)
async def my_loop():
    # будем выводить уастников в голосовых каналах
    # для каждого сервера из всех серверов, где есть бот
    for guild in bot.guilds:
        # выводим название сервера
        print(guild.name, end='')
        #              берем в генератор только тех участников, у которых свойство voice != None
        for member in (member for member in guild.members if member.voice):
            # выводим имя участника и название канала
            print(f'\t{member.name} ({member.voice.channel.name})')

# запускаем бота
bot.run('TOKEN')
