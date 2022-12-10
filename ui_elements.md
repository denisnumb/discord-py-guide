# Работа с кнопками и выпадающими списками.

Если вы все еще пользуетесь библиотекой `discord-py`, то для работы с материалами этого руководства вам придется обновиться на более актуальный форк этой библиотеки. Конкретно здесь пойдет речь про `PyCord`. Подробнее про смысл перехода на эту библиотеку [**здесь**][1].

---

Если кто не знал, в дискорд вместе со [*slash*-командами][1] уже давно завезли графические элементы, такие как:

- [Кнопки][2]

![image](https://user-images.githubusercontent.com/61795655/206858093-90e23edb-66e4-4786-8852-05b72897185f.png)

- [Выпадающие списки][3]

![image](https://user-images.githubusercontent.com/61795655/206858247-28bdb859-3445-4353-b989-87bcf7846729.png)

![image](https://user-images.githubusercontent.com/61795655/206858257-f67a805f-35f0-4736-93dc-10019770786e.png)

- [Диалоговые окна][4]

![image](https://user-images.githubusercontent.com/61795655/206858967-03f65415-ef25-4312-823d-0d8666aa29ea.png)


**Все эти элементы хранятся в модуле `discord.ui`** и работать с ними очень просто. *Для просмотра документации нажмите на интересующий элемент списка выше*

Для начала немного теории. Кнопки и выпадающие списки являются такими же элементами сообщения ([`discord.Message`][5]), как и вложения *(видео/изображения/файлы)* ([`discord.Message.attachments`][6]), Embed-формы ([`discord.Message.embeds`][7]) и прочие доп. элементы кроме основного текста.

Поэтому, когда вы отправляете сообщение с кнопкой, эту кнопку нужно куда-то размещать. Для этого в `PyCord` имеется специальный класс [`discord.ui.View`][8], который как раз таки будет содержать в себе все созданные в коде компоненты.

То есть, логика такая: 
1. Создаем экземпляр `View()`
2. Затем создаем объекты кнопок/выпадающих списков
3. Устанавливаем их внутрь формы `View` и уже эту форму передаем как параметр при отправке сообщения:

```py
view = . . .
await channel.send('Текст сообщения', view=view)
```

Дальше на конкретных примерах будет понятнее.

---

## Работа с кнопками

Кнопки имеют различные стили, которые хранятся в классе [`discord.ButtonStyle`][9]: 

![image](https://user-images.githubusercontent.com/61795655/206860608-3055ef61-ad56-49f8-b00f-33a0356dec24.png)

---

Импортируем из модуля `discord.ui` класс кнопки и класс формы для кнопки:

```py
from discord.ui import View, Button
```

Пусть кнопка создается при вызове команды `/test`:

```py
@bot.slash_command(name='create_button', description='Создает зеленую кнопку')
async def create_button_command(ctx: discord.ApplicationContext):
    . . .
```

---

Для начала создадим форму [`discord.ui.View`][8], в которую будем размещать кнопку. Из [документации][8] видим, что по умолчанию параметр `timeout` имеет значение `180.0`, что означает, что дискорд будет передавать боту информацию о нажатии на кнопку только в течение `180` секунд, а потом просто забудет про нее. Если вам нужно, чтобы бот работал с кнопкой все время, пока он запущен, то значение параметра следует установить как `None`

![image](https://user-images.githubusercontent.com/61795655/206860817-fded6bef-de83-4d2b-ad30-a0c6a0c99137.png)

```py
view = View(timeout=None)
```

---

Теперь давайте создадим кнопку. Из документации по классу [`discord.ui.Button`][2] видим, что можем передать в конструктор класса парамтры:

- `label`:      `str`                        — текст кнопки
- `emoji`:      [`discord.Emoji`][10]/`str`  — эмоджи рядом с текстом
- `style`:      [`discord.ButtonStyle`][9]   — стиль кнопки
- `custom_id`:  `str`                        — пользовательский идентификатор кнопки *(для удобства обработки нажатий)*
- `disabled`:   `bool`                       — состояние кнопки *(включена или выключена)*

*И другие параметры, про которые можно почитать в документации.*

Создаем объект кнопки:

```py
button = Button(label='Кнопка', style=discord.ButtonStyle.green)
```

---

### Обработчик нажатия на кнопку

Кнопка есть, теперь надо сделать, чтобы при нажатии на нее вызывалась какая-то функция. Сделаем, чтобы при нажатии на кнопку, текст сообщения отображал последнего пользователя, который ее нажал.

Реализуем это в функции `button_callback`:

Из [документации][12] видим, что при нажатии на кнопку, в обработчик будет передаваться аргумент `interaction` ([`discord.Interaction`][11]), из которого можно получить *пользовательский идентификатор кнопки*, *пользователя, который нажал на кнопку* и многое другое.

![image](https://user-images.githubusercontent.com/61795655/206861488-58d93f13-b2fd-4388-8901-be37e0acfbe3.png)

Не забываем указать, что функция принимает этот аргумент `interaction`.

```py
async def button_callback(interaction: discord.Interaction):
    await interaction.message.edit(content=f'Последним на кнопку нажал: {interaction.user.name}')
```

Далее присваиваем кнопке обработчик нажатия:

```py
button.callback = button_callback
```

Добавляем ее в форму `view`:

```py
view.add_item(button)
```

И отправляем ответ на команду:

```py
await ctx.respond(view=view)
```

---

Должно получиться как-то так *(код с пояснениями [здесь][13])*:

```py
import discord
from discord.ui import View, Button
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all())

async def button_callback(interaction: discord.Interaction):
    await interaction.message.edit(content=f'Последним на кнопку нажал: {interaction.user.name}')

@bot.slash_command(name='create_button', description='Создает зеленую кнопку', guild_ids=[752821563455176824])
async def create_button_command(ctx: discord.ApplicationContext):
    view = View(timeout=None)
    button = Button(label='Кнопка', style=discord.ButtonStyle.green)
    button.callback = button_callback
    view.add_item(button)

    await ctx.respond(view=view)


bot.run('TOKEN')
```

**Результат:**

![Untitled](https://user-images.githubusercontent.com/61795655/206863121-1c8c99b1-c42d-41cd-aeac-c609512dbad7.gif)


[1]: https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md#%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-slash-%D0%BA%D0%BE%D0%BC%D0%BC%D0%B0%D0%BD%D0%B4
[2]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Button
[3]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Select
[4]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Modal
[5]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message
[6]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message.attachments
[7]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message.embeds
[8]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.View
[9]: https://docs.pycord.dev/en/stable/api/enums.html#discord.ButtonStyle
[10]: https://docs.pycord.dev/en/stable/api/models.html#discord.Emoji
[11]: https://docs.pycord.dev/en/stable/api/models.html#discord.Interaction
[12]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Button.callback
[13]: https://github.com/denisnumb/discord-py-guide/blob/main/examples/button.py
