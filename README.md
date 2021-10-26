# 🗓️ TBot_calendar

Inline календарь на python для telegram ботов

Данный модуль представляет из себя готовое решение,

в полной мере обеспечивающий функционал требуемый от календаря.
##  ✨Функционал ##
Обзор всех функций можно найти здесь .
##  🚩Установка ##
Для установки пакета выполните следующую команду:
```
pip install python-telegram-bot-calendar
```
####  📃Использование ####

Для работы с модулем календаря, рассмотрим подключение его к боту на примере библиотеки `pyTelegramBotAPI`:

Существует один main class - `DetailedTelegramCalendar`

Подключаем модуль с помощью инструкции import

```python
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
```
В декораторе сообщений, создаем экземпляр модуля

```python
@bot.message_handler(commands=['start'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)
```
Обработаем запросы к модулю
```python
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
Для класса `DetailedTelegramCalendar`доступны следующие аргументы:

   - `calendar_id ` - целое число или строка, используемая для идентификации календаря.
   - Используется, когда вам нужно несколько разных календарей (по умолчанию - 0)
 
   - `current_date` - `datetime.date`, начальное значение даты (по умолчанию - текущая дата)

   - `additional_buttons` - одномерный список кнопок, которые будут добавлены в конец календаря

   - `locale` - `en`, `ru` или `ukr`, выбор локализации модуля

   - `min_date` и `max_date` - оба используются как минимальное и максимальное значения для календаря

Использование указанных аргументов возможно в декораторе callback_query_handler

Это сработает автоматически

Функция принимает только один аргумент - `calendar_id`, который по умолчанию равен 0.


В теле функции-обработчика вам нужно вызвать функцию процесса для данных обратного вызова. 

ПРЕДУПРЕЖДЕНИЕ! Вам нужно создать объект календаря заново, если он не был сохранен ранее.

Функция `process` возвращает строку/ряд из трех пунктов - `result`, `keyboard`, `step`.

   - `result` - `datetime.date` объект, если пользователь завершил выбор. В противном случае - `None`

   - `keyboard` - inline keyboard markup если выбор не готов. В противном случае - `None`

   - `step` - `YEAR`, `MONTH`, или `DAY` если выбор не готов. Значение `None` также возможно, если нет изменений в клавиатуре.


## Authors
shamandok - @shamandok

## 📝 License

Copyright © 2020 [artembakhanov](https://github.com/artembakhanov). <br />
This project is [MIT](https://github.com/avneesh0612/next-progress-bar/blob/main/LICENSE) licensed.
