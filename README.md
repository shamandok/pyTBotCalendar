# <p align="center">:calendar: pyTBotCalendar</p>
<p align="center"> Календарь для telegram бота</p>
<p align="center"> с поддержкой мультиязычности и возможностью кастомизации.</p>

##  🚩Установка ##
Пакет протестирован с Python 3.6-3.8
   - Установка с помощью pip (менеджер пакетов Python):
```
pip install python-telegram-bot-calendar
```
Для работы с пакетом календаря, рассмотрим подключение его к боту на примере библиотеки `pyTelegramBotAPI`:

   - Подключаем пакет с помощью инструкций from и import

```python
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
```
   - В обработчике сообщений, вызовем экземпляр календаря

```python
@bot.message_handler(commands=['start'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)
```
   - Добавим обработчик callback_query запросов и ответы на них
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

Использование указанных аргументов возможно в обработчике callback_query запросов

Это сработает автоматически

Функция принимает только один аргумент - `calendar_id`, который по умолчанию равен 0.


В теле функции-обработчика вам нужно вызвать функцию процесса для данных обратного вызова. 

ПРЕДУПРЕЖДЕНИЕ! Вам нужно создать объект календаря заново, если он не был сохранен ранее.

Функция `process` возвращает строку/ряд из трех пунктов - `result`, `keyboard`, `step`.

   - `result` - `datetime.date` объект, если пользователь завершил выбор. В противном случае - `None`

   - `keyboard` - inline keyboard markup если выбор не готов. В противном случае - `None`

   - `step` - `YEAR`, `MONTH`, или `DAY` если выбор не готов. Значение `None` также возможно, если нет изменений в клавиатуре.

##  ⭐Планы ##
|      Модуль     | Описание                 | Заметки                       |  Статус |
| :-------------: |:------------------------:|:-----------------------------:|:-------:|
| Локализация     | Поддержка других языков  |    (RU/END/UKR)               |    🧮   |
| Уровни доступа  | Возможности пользователей|   (User/Moderator/Admin)      |    🧮   |
| WEB-Панель      | Управление ботом         |           (AdminPanel)        |    🧮   |
|      WEB        | Страница обьявлений      |             (Site)            |    🧮   |


|       ℹ️     |            ℹ️       |         ℹ️       |       ℹ️         |        ℹ️         |
| :---------:|:------------------:|:---------------:|:---------------:|:---------------:|
|  ✔️сделано |    🛠️ В работе    |   🧮 В очереди  |  ⚡ Отладка    |    ❌Отменено   |

## Автор
Artem Moskalenko - [@shamandok](https://github.com/shamandok) <br />

## 📝 Лицензия

Copyright © 2020 [artembakhanov](https://github.com/artembakhanov). <br />
This project is [MIT](https://github.com/shamandok/Python-TBot-calendar/blob/main/LICENSE) licensed.
