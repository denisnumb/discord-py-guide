import discord
from discord import SelectOption
from discord.ui import View, Select
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all())

# обработчик выбора элемента из выпадающего списка
# подробнее: https://github.com/denisnumb/discord-py-guide/blob/main/ui_elements.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA-%D0%B2%D1%8B%D0%B1%D0%BE%D1%80%D0%B0-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%B0
async def select_callback(interaction: discord.Interaction):
    # из объекта interaction получаем объект сообщения и вызываем у него метод изменения (edit)
    # затем изменяем текст сообщения, подставляя туда имя пользователя, который выбрал параметр из списка
    # и сам выбранный параметр
    await interaction.message.edit(content=f'{interaction.user.name} выбрал {interaction.data["values"][0]}')

# команда для создания выпадающего списка
# подробнее про эту команду: https://github.com/denisnumb/discord-py-guide/blob/main/ui_elements.md#%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-%D1%81-%D0%B2%D1%8B%D0%BF%D0%B0%D0%B4%D0%B0%D1%8E%D1%89%D0%B8%D0%BC%D0%B8-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0%D0%BC%D0%B8
# подробнее про slash-команды в целом: https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md
@bot.slash_command(name='create_select_menu', description='Создает выпадающий список', guild_ids=[752821563455176824])
async def create_button_command(ctx: discord.ApplicationContext):
    # создаем форму, в которой будет размещена кнопка
    view = View(timeout=None)
    
    # создаем выпадающий список с 3 элементами
    select = Select(
        options=[
            SelectOption(label='Яблоко', emoji='🍏', default=True),
            SelectOption(label='Банан', emoji='🍌'),
            SelectOption(label='Апельсин', emoji='🍊'),
        ]
    )
    
    # задаем списку обработчик выбора параметра
    select.callback = select_callback
    # добавляем список на форму view
    view.add_item(select)

    await ctx.respond(view=view)

# запускаем бота
bot.run('TOKEN')
