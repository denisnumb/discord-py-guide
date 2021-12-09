Если функционал вашего бота рассчитан не только на работу с текстом сообщений, но и на обработку отдельных команд, то в качестве бота стоит использовать не [`discord.Client`][1], а [`discord.ext.commands.Bot`][2], который умеет обрабатывать отельные команды.

Подробнее про различия можно почитать [**здесь**][3].

---

## И вместо такой реализации команд
```py
@bot.event
async def on_message(message):
  if message.author.bot:
    return
    
  if message.content == '!test':
    # код для команды !test
```

## Стоит использовать такую

```py
@bot.command()
async def test(ctx):
  # код для команды !test
```

Подробнее про создание команд можно почитать [**здесь**][3].

---

## Почему не стоит обрабатывать команды через `on_message()`?

1. В `discord-py` заранее предусмотрена возможность обрабатывать команды через отдельные функции, поэтому не стоит усложнять себе жизнь
2. Если вам потребуется сложная команда, с необходимостью приема нескольких значений, это гораздо проще реализовать через отдельную функцию, чем писать разделение аргументов самостоятельно
3. При большом количестве команд, прописывать все в одной функции будет некорректно с точки зрения написания кода.


[1]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=client#discord.Client
[2]: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=bot#discord.ext.commands.Bot
[3]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-%D0%B1%D0%BE%D1%82%D0%BE%D0%BC-%D0%B8-discord-py
[4]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4
