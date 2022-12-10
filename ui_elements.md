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

- `discord.ButtonStyle.blurple`: ![image](https://user-images.githubusercontent.com/61795655/206860355-c93f825c-5d67-4f2b-a6b5-6a3cde60dd3f.png)
- `discord.ButtonStyle.gray`: ![image](https://user-images.githubusercontent.com/61795655/206860436-eb015c4f-91e6-4915-887b-43feaa2e6338.png)
- `discord.ButtonStyle.green`: ![image](https://user-images.githubusercontent.com/61795655/206860470-428a05b0-4deb-40e2-96b0-d1f3f1ac5fb2.png)
- `discord.ButtonStyle.red`: ![image](https://user-images.githubusercontent.com/61795655/206860483-a794d199-2233-4e1c-84ed-fa592f4abecb.png)
- `discord.ButtonStyle.link`: ![image](https://user-images.githubusercontent.com/61795655/206860488-40c33134-f30f-49d1-b08d-cbe7c51b81d1.png)

Импортируем из модуля `discord.ui` класс кнопки и класс формы для кнопки:

```py
from discord.ui import View, Button
```



[1]: https://github.com/denisnumb/discord-py-guide/blob/main/slash-commands.md#%D1%80%D0%B5%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-slash-%D0%BA%D0%BE%D0%BC%D0%BC%D0%B0%D0%BD%D0%B4
[2]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Button
[3]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Select
[4]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.Modal
[5]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message
[6]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message.attachments
[7]: https://docs.pycord.dev/en/stable/api/models.html#discord.Message.embeds
[8]: https://docs.pycord.dev/en/stable/api/ui_kit.html#discord.ui.View
[9]: https://docs.pycord.dev/en/stable/api/enums.html#discord.ButtonStyle
