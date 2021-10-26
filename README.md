# 🗓️ TBot_calendar

Inline календарь на python для telegram ботов
##  ✨Функционал ##
Обзор всех функций можно найти здесь .
##  🚩Установка ##
Для установки пакета в систему выполните следующую команду:
```
pip install python-telegram-bot-calendar
```
####  📃Вступление ####

Данный модуль представляет из себя готовое решение, в полной мере обеспечивающий функционал требуемый от календаря.

Для использования или изминения функционала, необходимо понимать его структуру.

В роли главного или исполняемого класса выступает DetailedTelegramCalendar

Использование

Для начала работы с модулем календаря, подключим его к боту на примере библиотеки pyTelegramBotAPI:


```python
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP

...
@bot.message_handler(commands=['start'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)

```

В декораторе 'bot.message_handler' `Код` создается календарь.
Можно передать несколько аргументов:
calendar_id - маленькое целое число или строка, используемая для идентификации календаря. Используется, когда вам нужно несколько разных календарей (по умолчанию - 0)
current_date - объект datetime.date, начальное значение даты (по умолчанию - сегодняшняя дата)
additional_buttons - одномерный список кнопок, которые будут добавлены в конец календаря
locale - en, ru или eo, можно добавить еще
min_date и max_date - оба используются как минимальное и максимальное значения для календаря
Как видите, предоставленная специальная функция должна быть передана обработчику запроса обратного вызова. Это сработает автоматически. Функция принимает только один аргумент - calendar_id, который по умолчанию равен 0.


In the body of the handler function you need to call process function on callback data. WARNING! You need to create the calendar object again if it was not saved before.

The function process return tuple of size 3 - result, keyboard, step.

result - datetime.date object if user finished selecting. Otherwise None
keyboard - inline keyboard markup if the result is not ready. Otherwise None
step - YEAR, MONTH, or DAY if not ready. None is also possible if there is no change in keyboard.
Advanced use
Several calendars
You can create as many calendars as you want. However, in order to handle them properly set different calendar_id's when you want to distinguish them. Take a look at examples.

Date ranges
In the class constructor min_date and max_date - both are used as min and max values for the calendar. If you add them, the calendar will not show undesired dates. Example:
Custom style
You can also write your own code. One of the examples is redefining the steps order.

In the package you can find WMonthTelegramCalendar and WYearTelegramCalendar that start from day and month selecting, not from year.

You can also redefine style parameters. Example:
Custom Translation
