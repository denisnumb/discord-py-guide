# Руководство по использованию [документации][7] `discord-py`

Абсолютно каждый объект дискорда, с которым взаимодействует ваш бот, представлен в библиотеке `discord` в виде отдельного класса.

Когда вы получаете сообщение из функции-события `on_message(message)`, аргумент `message` имеет является классом библиотеки `discord` и имеет тип [`discord.Message`][1].

Точно также свои типы имеют **пользователь** ([`discord.User`][2]), **сервер** ([`discord.Guild`][3]), **участник сервера** ([`discord.Member`][4]), **роль** ([`discord.Role`][5]) и другие объекты.

---

### Распространенная ошибка

**Подобный тип ошибки встречается чаще всего у тех пользователей, которые ни разу не открывали [документацию][7].**

Предположим, вы получили сообщение через обработчик `on_message(message)` и хотите узнать что написано в этом сообщении. Вы выводите его при момощи строчки `print(message)`, но вместо ожидаемого результата получаете что-то такое:
```
<Message id=917324421392928266 channel=<TextChannel id=760430076071690856 name='тест-бота' position=6 nsfw=False news=False category_id=842698448217964574> type=<MessageType.default: 0> author=<Member id=344865227062144141 name='name' discriminator='1234' bot=False nick='nickname' guild=<Guild id=752821563455176824 name='Server' shard_id=None chunked=True membe
r_count=10000>> flags=<MessageFlags value=0>>
```

Это произошло потому что сам по себе объект `message` не является строкой (`str`), содержащей текст сообщения. Он является объектом [`discord.Message`][1], который содержит в себе другие объекты библиотеки `discord`, такие как **автор сообщения** (который в свою очередь является объектом [`discord.User`][2] или [`discord.Member`][4], в зависимости от контекста), **канал** ([`discord.TextChannel`][6]), **текст сообщения** (который является строкой (`str`)) и [другие][1] свойства.

---

### Как пользоваться [документацией][7]

Чтобы избежать проблемы, приведенной выше и не гадать, как же получить какое-либо свойство объекта (*текст сообщения*, *цвет роли* или *id пользователя*) можно один раз научиться пользоваться документацией.

1. Заходим на главную страницу документации: https://discordpy.readthedocs.io/en/stable/index.html

Здесь видим область поиска, в которую нужно ввести название интересующего нас в данный момент объекта. Допустим, мы работаем с объектом сообщения. Напишем в поиске `message`  нажмем <kbd>Enter</kbd>

![1](https://user-images.githubusercontent.com/61795655/144809560-ca18d073-0819-4042-8c0f-fee37e07261e.png)

2. Здесь видим кучу разных объектов, однако нас интересует именно чистый класс [`discord.Message`][1], так как, например, элемент списка `discord.Reaction.message` является всего лишь свойством другого класса [`discord.Reaction`][8] и ссылается на тот же класс [`discord.Message`][1]. Вы можете убедиться в этом самостоятельно открыв страницу. 

![image](https://user-images.githubusercontent.com/61795655/144810003-3bf5e262-d7b0-46de-83df-d1fb9d8835ff.png)

3. Открываем [`discord.Message`][1] и получаем всю информацию об объекте. В колонке **Attributes** вы можете видеть все свойства объекта сообщения. Здесь все, что описывалось 

![image](https://user-images.githubusercontent.com/61795655/144810658-8ed37216-d044-4087-b886-fe0ff81fedcd.png)


[1]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.Message
[2]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.User
[3]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Guild
[4]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Member
[5]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=guild#discord.Role
[6]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.TextChannel
[7]: https://discordpy.readthedocs.io/en/stable/index.html
[8]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=message#discord.Reaction
