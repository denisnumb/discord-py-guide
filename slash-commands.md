# Реализация slash-комманд

*Если вы только начали изучать работу с библиотекой, то рекомендую сначала изучить [**основное руководство**][41] или хотя бы [**основы *prefix*-команд**][42]* 

---
 
 На этом этапе надо отметить, что `discord-py` — устаревшая библиотека, которая не обновляется под новые фишки дискорда. Поэтому для работы со *slash*-командами, кнопками и выпадающими списками стоит удалить старую библиотеку и установить ее форк `PyCord`:
 ```cmd
 pip install py-cord==2.0.0b5
 ```
В целом, вся структура классов, их свойств и методов в `PyCord` осталась такой же как в `discord-py`, поэтому ничего менять и переписывать не нужно. Поэтому к `PyCord` подойдет документация от `discord-py`, но я все же рекомендую пользоваться [**документацией**][35] именно от `PyCord`

Для реализации *slash*-команд, в качестве объекта бота можно использвать все тот же класс [`discord.ext.commands.Bot`][7].

Для *slash*-команд, остаются актуальными все свойства *prefix-команд*. Разве что, декоратор `@bot.command()` меняется на `@bot.slash_command()`

## Первая *slash*-команда

Декоратор `@bot.slash_command()` принимает некоторые необязательные аргументы. Рассмотрим следующие:

- `name`: название команды
- `description`: описание команды
- `guild_ids`: список `id` серверов, на которых эта команда будет доступна. Поскольку *slash*-команды синхронизируются с дискордом, данный параметр также имеет смысл указывать для ускорения процесса синхронизации. ([**Подробный разбор проблемы**][39])

Теперь приступим к созданию команды. В декоратор можно сразу передать параметры **названия** и **описания**:
```py
@bot.slash_command(name='test_slash_command', description='Описание команды')
```
Конечно, там есть много других параметров, описание которых можно найти в документации по [`discord.SlashCommand`][36]

Далее создаем функцию команды. Поскольку дискорд обрабатывает команды интерактивно,

![1](https://user-images.githubusercontent.com/61795655/206871309-5a8f7fd9-6030-43ac-aa72-78db0d4432c6.gif)

необходимо что-то делать с контекстом выполнения команды:

Либо его можно удалить (`await ctx.delete()`):
```py
@bot.slash_command(name='test_slash_command', description='Удаляет контекст и выводит сообщение "Успешный тест!"')
async def __test(ctx):
    await ctx.delete()
    await ctx.send('Успешный тест!')
```

**Результат:**

![2 (1)](https://user-images.githubusercontent.com/61795655/206871795-d6bd5bdb-39ee-4ea7-be23-b84863f7771f.gif)

Либо отправить ответ сразу (`await ctx.respond()`):
```py
@bot.slash_command(name='test_slash_command', description='Отвечает "Успешный тест!"')
async def __test(ctx):
    await ctx.respond('Успешный тест!')
```

**Результат:**
 
![3](https://user-images.githubusercontent.com/61795655/206872087-f27b668f-e7fb-4f89-ab83-09471bab1292.gif)

Если не сделать что-то с конекстом, то дискорд не дождавшись ответа от бота, выдаст ошибку. Например, вот такая команда, которая ничего не возвращает, а просто осуществляет вывод в консоль

```py
@bot.slash_command(name='test_slash_command', description='Выполняет print(\'Команда выполнена!\')')
async def __test(ctx):
    print('Команда выполнена!')
```

Действительно выведет сообщение в консоль, но вот обработка команды в дискорде будет выглядеть так:

![4](https://user-images.githubusercontent.com/61795655/206872103-5918c39b-2df5-4257-af4d-d3ab84e32fa8.gif)

Выглядит так, будто при выполнении произошла ошибка, но на деле это просто дискорд не получил ответа от бота. Однако это может произойти даже если команда подразумевает ответ. Например, если идут какие-то долгие вычисления, дискорд может просто не дождаться ответа и команда не выполнится. В таких случаях контекст стоит либо удалять, как показано в примере выше, либо использовать метод контекста [`defer()`][37]. 

Из описания следует, что он нужен как раз для таких ситуаций: "*Откладывает ответ на взаимодействие. Обычно это используется, когда взаимодействие подтверждено, а дополнительное действие будет выполнено позже.*"

```py
import asyncio
. . .

@bot.slash_command(name='test_slash_command', description='Имитирует 5-секундное вычисление и выводит "Команда выполнена!"')
async def __test(ctx):
    await ctx.defer()
    await asyncio.sleep(5)
    await ctx.respond('Команда выполнена!')
```

**Результат:**

![5](https://user-images.githubusercontent.com/61795655/206872116-090ad003-f853-450b-bc13-864cbd4cbd00.gif)

Разумеется, использовать метод `await ctx.defer()` имеет смысл только если вы собираетесь что-то отвечать на команду. Если же никакого ответа не подразумевается, то лучше просто удалять контекст. Иначе бот просто бесконечно будет "думать" как на скрине выше.

## Работа с аргументами

Работа с аргументами у *slash*-команд устроена иначе, нежели у *prefix*-команд. Чтобы `PyCord` распознал аргумент и передал его в дискорд, нужно в качестве аннотации типа аргумента команды указать экземпляр класса [`discord.Option`][38]

Для начала импортируем класс в код
```py
from discord import Option
```

Конструктор класса `Option` принимает некоторые параметры. В основном указывают следующие:

- тип аргумента
- `name`: название аргумента *(Наследуется от имени переменной, если оно не указано в качестве параметра.)*
- `description`: описание аргумента 
- `required`: обязательно ли указывать этот аргумент при вызове команды (`True`/`False`)
- `default`: стандартное значение аргумента, если он не был указан

Также есть следующие:

- `min_value`: минимальное число, которое пользователь может ввести в качестве аргумента *(если тип аргумента — `int`/`float`)*
- `max_value`: тоже самое, что и `min_value`, только это верхняя граница — максимальное число
- `choices`: список (`list`) значений аргумента, которые пользователь может выбрать
- `min_length`: минимальная длина строки, которую пользователь должен ввести в качестве значения аргумента

Есть и другие параметры, про которые все также можно почитать в документации к [`discord.Option`][38]. *Некоторые из них будут разобраны позже.*

Таким образом, получение любого аргумента будет выглядеть так:

```py
@bot.slash_command()
async def test(ctx, arg: Option(str)):
    . . .
```

Теперь давайте попробуем получить от пользователя следующие аргументы:

1. Число в диапазоне от 1 до 10
2. Значение типа `bool`
3. Участника сервера ([`discord.Member`][31])
4. Текст из нескольких слов
5. Слово из списка для выбора 

Реализация аргументов будет выглядеть так:

```py
@bot.slash_command(name='test_slash_command')
async def __test(
    ctx,
    number:  Option(int,             description='Число в диапазоне от 1 до 10', required=True,  min_value=1, max_value=10),
    member:  Option(discord.Member,  description='Любой участник сервера',       required=True),
    choice:  Option(str,             description='Выберите пункт из списка',     required=True,  choices=['Банан', 'Яблоко', 'Апельсин']),
    text:    Option(str,             description='Текст из нескольких слов',     required=False, default=''),
    boolean: Option(bool,            description='True или False',               required=False, default=False)
    ):
    await ctx.delete()
    
    for argument in (number, boolean, member, text, choice):
        print(f'{argument} ({type(argument).__name__})\n')
```

**Результат:**

Обратите внимание:

- Аргументы можно указывать в разном порядке
- Встроенная проверка не даст ввести некорректное значение
- Необязательные *(`required=False`)* параметры можно не указывать

![6](https://user-images.githubusercontent.com/61795655/206872158-6975be7a-19df-48b6-acee-99964bc4300d.gif)

На выходе получаем:
```cmd
5 (int)
False (bool)
dennys#0000 (Member)
Текст с пробелами (str)
Яблоко (str)
```

## Пользовательские типы аргументов

Предположим, вам нужно получить от пользователя `bool`-значение. Чтобы не указывать в описании аргумента за что отвечает `True`, а за что `False`, можно написать свой тип аргумента, который будет предлагать пользователю выбор `Да`/`Нет` (Вместо `True`/`False`), затем автоматически конвертировать выбор в `bool`.

Для этого создадим новый статический класс, который будет наследоваться от [`discord.ext.commands.Converter`][40]. 

Класс должен переопределять метод `convert`, принимающий аргументы: 

- `cls` — объект этого класса
- `ctx` — контекст выполнения команды
- `arg` — значение аргумента

Данный метод будет конвертировать полученную строку (`str`) `'Да'`/`'Нет'` в `bool` в зависимоси от значения.

Также внутри класса можно сразу создать поле `choices`, содержащее варианты выбора:

```py
class CustomBoolArgType(commands.Converter):
    choices = ('Да', 'Нет')

    async def convert(cls, ctx, arg):
        return arg == 'Да'
```

Теперь подставим его в качестве типа аргумента. В параметр `choices` передадим значение поля класса:

```py
@bot.slash_command()
async def test(ctx, arg: Option(CustomBoolArgType, choices=CustomBoolArgType.choices)):
    await ctx.respond(f'{arg}, {type(arg).__name__}')
```

**Результат:**

![7](https://user-images.githubusercontent.com/61795655/206872185-a4c473ec-5e56-43bc-9dd1-c346ae733e50.gif)

Разумеется, можно делать и более сложные конвертации во что угодно, буквально ограничиваясь своей фантазией и необходимостью. Вот пример преобразования слова в число:

```py
class IntFromStrArgType(commands.Converter):
    values = ('Один', 'Два', 'Три')

    async def convert(cls, ctx, arg):
        try:
            return cls.values.index(arg) + 1
        except ValueError:
            return -1

@bot.slash_command()
async def test(ctx, arg: Option(IntFromStrArgType)):
    await ctx.respond(f'{arg}, {type(arg).__name__}')
```

**Результат:**

![8](https://user-images.githubusercontent.com/61795655/206872189-2fb4d7af-9c54-409f-a387-b73f0e65073b.gif)

[7]: https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=bot#discord.ext.commands.Bot
[31]: https://discordpy.readthedocs.io/en/stable/api.html?highlight=member#discord.Member
[34]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%B8%D0%BD%D0%B8%D1%86%D0%B8%D0%B0%D0%BB%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D0%B1%D0%BE%D1%82%D0%B0
[35]: https://docs.pycord.dev/en/stable/index.html
[36]: https://docs.pycord.dev/en/stable/api/application_commands.html#discord.SlashCommand
[37]: https://docs.pycord.dev/en/stable/api/application_commands.html#discord.ApplicationContext.defer
[38]: https://docs.pycord.dev/en/stable/api/application_commands.html#id7
[39]: https://github.com/denisnumb/discord-py-guide/blob/main/problems/slash_command_not_update.md
[40]: https://docs.pycord.dev/en/stable/ext/commands/api.html#discord.ext.commands.Converter
[41]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E-%D0%B1%D0%B8%D0%B1%D0%BB%D0%B8%D0%BE%D1%82%D0%B5%D0%BA%D0%B8-discord-py
[42]: https://github.com/denisnumb/discord-py-guide/blob/main/discord-py.md#%D0%BE%D0%B1%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B0-%D0%BE%D1%82%D0%B4%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D1%85-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4
