# 📅 TBot_calendar

Inline календарь на python для telegram ботов

Getting Started
This library is tested on Python 3.6 and 3.7.

Installation
pip install python-telegram-bot-calendar
Usage
There is one main class - DetailedTelegramCalendar that can be used as follows. This is the example for pyTelegramBotAPI library. Other libraries are also supported.
In start handler the calendar is created. Several arguments can be passed:

calendar_id - small integer or string, used for calendar identification. It used when you need several different calendars (default - 0)
current_date - datetime.date object, initial date value (default - today date)
additional_buttons - 1D list of buttons that will be added to the bottom of the calendar
locale - either en, ru, or eo, can be added more
min_date and max_date - both are used as min and max values for the calendar
As you can see, special function that is provided should be passed to callback query handler. It will automatically work. The function takes only one argument - calendar_id that is 0 by default.

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
