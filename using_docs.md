# Руководство по использованию [документации][7] `discord-py`

Абсолютно каждый объект дискорда, с которым взаимодействует ваш бот, представлен в библиотеке `discord` в виде отдельного класса.

Когда вы получаете сообщение из функции-события `on_message(message)`, аргумент `message` является классом библиотеки `discord` и имеет тип [`discord.Message`][1].

Точно также свои типы имеют **пользователь** ([`discord.User`][2]), **сервер** ([`discord.Guild`][3]), **участник сервера** ([`discord.Member`][4]), **роль** ([`discord.Role`][5]) и другие объекты.

---

### Распространенная ошибка

**Подобный тип ошибки встречается чаще всего у тех пользователей, которые ни разу не открывали [документацию][7].**

Предположим, вы получили сообщение через обработчик `on_message(message)` и хотите узнать что написано в этом сообщении. Вы выводите его при момощи строчки `print(message)`, но вместо ожидаемого результата получаете что-то такое:
```py
<Message id=917324421392928266 channel=<TextChannel id=760430076071690856 name='тест-бота' position=6 nsfw=False news=False category_id=842698448217964574> type=<MessageType.default: 0> author=<Member id=344865227062144141 name='name' discriminator='1234' bot=False nick='nickname' guild=<Guild id=752821563455176824 name='Server' shard_id=None chunked=True membe
r_count=10000>> flags=<MessageFlags value=0>>
```

Это произошло потому что сам по себе объект `message` не является строкой (`str`), содержащей текст сообщения. Он является объектом [`discord.Message`][1], который содержит в себе другие объекты библиотеки `discord`, такие как **автор сообщения** (который в свою очередь является объектом [`discord.User`][2] или [`discord.Member`][4], в зависимости от контекста), **канал** ([`discord.TextChannel`][6]), **текст сообщения** (который является строкой (`str`)) и [другие][1] свойства.

Чтобы не допускать подобных ошибок, я рекомендую почитать гайд по использованию документации, который приведен ниже

---

### Как пользоваться [документацией][7]

Чтобы избежать проблемы, приведенной выше и не гадать, как же получить какое-либо свойство объекта (*текст сообщения*, *цвет роли* или *id пользователя*) можно один раз научиться пользоваться документацией.

1. Заходим на главную страницу документации: https://discordpy.readthedocs.io/en/stable/index.html

Здесь видим область поиска, в которую нужно ввести название интересующего нас в данный момент объекта. Допустим, мы работаем с объектом сообщения. Напишем в поиске `message`  нажмем <kbd>Enter</kbd>

![1](https://user-images.githubusercontent.com/61795655/144809560-ca18d073-0819-4042-8c0f-fee37e07261e.png)

2. Здесь видим кучу разных объектов, однако нас интересует именно чистый класс [`discord.Message`][1], так как, например, элемент списка `discord.Reaction.message` является всего лишь свойством другого класса [`discord.Reaction`][8] и ссылается на тот же класс [`discord.Message`][1]. Вы можете убедиться в этом самостоятельно открыв страницу. 

![image](https://user-images.githubusercontent.com/61795655/144810003-3bf5e262-d7b0-46de-83df-d1fb9d8835ff.png)

3. Открываем [`discord.Message`][1] и получаем всю информацию об объекте. В колонке **Attributes** вы можете видеть все свойства объекта сообщения. Здесь все, что описывалось в [**примере выше**][9]. В колонке **Methods** все функции, которые можно вызвать у объекта сообщения.

![image](https://user-images.githubusercontent.com/61795655/144810658-8ed37216-d044-4087-b886-fe0ff81fedcd.png)

4. Нажав на любой элемент из колонки **Attributes** или **Methods**, вы переместитесь к более подробному описанию свойства или метода.

Например, тыкнем на `channel` и увидем, что это свойство `discord.Message.channel` по сути является другим объектом библиотеки [`discord.TextChannel`][6], нажав на который мы можем открыть и посмотреть его свойства и методы

![image](https://user-images.githubusercontent.com/61795655/144811568-290b9163-703d-4887-94c1-c62b2d8dddb0.png)

5. К примеру, у текстового канала, видим асинхронный метод `send`

![image](https://user-images.githubusercontent.com/61795655/144811950-cc7ef98a-369b-4ec1-830e-e0d2f77c8243.png)

6. Открыв его, можем увидеть подробное описание самой функции, аргументов, которые она принимает, что возвращает и т.д.

Теперь видим, что единственным обязетальным аргументом является `content`, который принимает тип `str` и явлвяется текстом отправляемого сообщения

![image](https://user-images.githubusercontent.com/61795655/144812168-3b3ca691-15d7-4605-a44f-b88a5c025e6d.png)

---

Думаю, очевидно, что работа с остальными объектами полностью аналогична. Ищите по ключевому слову объект, про который вам нужно узнать, смотрите чт ос ним можно сделать и делаете :)

В итоге, потыкав пару минут документацию, вы на вряд ли будете допускать базовые ошибки и задавать повторяющиеся вопросы на [стаке][10] или других площадках.

```py
@bot.event
async def on_message(message):
  # из документации находим, что текст сообщения содержится в свойстве content
  print(f'Текст сообщения: {message.content}')
  # из объекта сообщения получаем канал, в котором это сообщение находится и у канала вызываем метод send
  await message.channel.send('Отправка сообщения в ответ!')
```

[1]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.Message
[2]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.User
[3]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Guild
[4]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Member
[5]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Role
[6]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.TextChannel
[7]: https://discordpy.readthedocs.io/en/stable/index.html
[8]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.Reaction
[9]: https://github.com/denisnumb/discord-py-guide/blob/main/using_docs.md#%D1%80%D0%B0%D1%81%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D0%B0
[10]: https://ru.stackoverflow.com/
