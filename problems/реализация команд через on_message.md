Если функционал вашего бота рассчитан не только на работу с текстом сообщений, но и на обработку отдельных команд, то в качестве бота стоит использовать не [`discord.Client`][1], а [`discord.ext.commands.Bot`][2], который умеет обрабатывать отельные команды.

Подробнее про различия ботов можно почитать [**здесь**][3].

Подробнее про создание команд можно почитать [**здесь**][4].

---

## Почему не стоит обрабатывать команды через `on_message()`?

1. В `discord-py` заранее предусмотрена возможность обрабатывать команды через отдельные функции, поэтому не стоит усложнять себе жизнь
2. Если вам потребуется сложная команда, с необходимостью приема нескольких значений, это гораздо проще реализовать через отдельную функцию, чем писать разделение аргументов самостоятельно
3. При большом количестве команд, прописывать все в одной функции будет некорректно с точки зрения написания кода.

*Просто представьте, что вы пишете текст документа не в Word, а в ячейках Excel. Это же использование инструмента не по назначению! Вот и здесь также.*

## Пример:

Команда принимает через пробелы первым аргументом *упоминание пользователя*, вторым *число*, третьим весь остальной текст, с учетем пробелов.

**Выглядит это так:**

![image](https://user-images.githubusercontent.com/61795655/145382386-a441072c-4c1a-4849-90e9-fa27ec9f32c5.png)

**Реализация через `on_message()`** - все аругменты приходится получать вручную
```py
@bot.event
async def on_message(message):  
  if message.content.startswith('!command'):
    # message.content.split() = ['!command', '<@!249864127063142451>', '2', 'текст', 'с', 'пробелами']
    member = message.mentions[0]
    number = int(message.content.split()[2])
    text = ' '.join(message.content.split()[3:])
```

**Реализация через отдельную функцию** - `discord-py` все делает за вас
```py
@bot.command()
async def command(ctx, member: discord.Member, number: int, *, text):
  # Готово! Переменные уже получены в качестве аргументов и имеют те же типы
```

**Как видно, в данном случае реализация через отдельную функцию гораздо компактнее и удобнее**

[1]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=client#discord.Client
[2]: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=bot#discord.ext.commands.Bot
[3]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D1%81-%D0%B1%D0%BE%D1%82%D0%BE%D0%BC-%D0%B8-discord-py
[4]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4
