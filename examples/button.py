import discord
from discord.ui import View, Button
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all())

# обработчик нажатия на кнопку
# подробнее: https://github.com/denisnumb/discord-py-guide/blob/main/ui_elements.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA-%D0%BD%D0%B0%D0%B6%D0%B0%D1%82%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D1%83
async def button_callback(interaction: discord.Interaction):
    # из объекта interaction получаем объект сообщения и вызываем у него метод изменения (edit)
    # затем изменяем текст сообщения, подставляя туда имя пользователя, который нажал на кнопку
    await interaction.message.edit(content=f'Последним на кнопку нажал: {interaction.user.name}')

# команда для создания кнопки
# подробнее про эту команду: https://github.com/denisnumb/discord-py-guide/blob/main/ui_elements.md#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%BA%D0%BD%D0%BE%D0%BF%D0%BA%D0%B0%D0%BC%D0%B8
# подробнее про slash-команды в целом: https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md
@bot.slash_command(name='create_button', description='Создает зеленую кнопку', guild_ids=[752821563455176824])
async def create_button_command(ctx: discord.ApplicationContext):
    # создаем форму, в которой будет размещена кнопка
    view = View(timeout=None)
    # создаем кнопку и устанавливаем для нее обработчик нажатия (свойство callback)
    button = Button(label='Кнопка', style=discord.ButtonStyle.green)
    button.callback = button_callback
    # добавляем кнопку на форму view
    view.add_item(button)

    await ctx.respond(view=view)

# запускаем бота
bot.run('TOKEN')
