Если ваши *slash*-команды не обновляеются после запуска бота, для начала убедитесь, что они [правильно оформлены][1].

Если все верно, то скорее всего дело в том, что дискорду нужно время, чтобы синхронизировать ваши команды с графическим интерфейсом. 

Чтобы ускорить этот процесс, вы можете указать в дектораторе `@bot.slash_command()` параметр `guild_ids`, в котором явно укажите список серверов, на которых должна обновляться команда:

```py
@bot.slash_command(name='command', description='description', guild_ids=[4786287623874688236])
async def my_slash_command(ctx):
    . . .
```

Теперь команды будут синхронизироваться сразу же после запуска бота

[1]: [https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-slash-%D0%BA%D0%BE%D0%BC%D0%BC%D0%B0%D0%BD%D0%B4](https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md#%D0%BF%D0%B5%D1%80%D0%B2%D0%B0%D1%8F-slash-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0)](https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md#%D0%BF%D0%B5%D1%80%D0%B2%D0%B0%D1%8F-slash-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D0%B0)
