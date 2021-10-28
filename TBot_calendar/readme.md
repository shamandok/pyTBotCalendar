def last_day_month(year, month):
    leap_year_flag = 0
    end_dates = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # Checking for regular leap year
    if year % 4 == 0:
        leap_year_flag = 1
    else:
        leap_year_flag = 0

    # Checking for century leap year
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year_flag = 1
        else:
            leap_year_flag = 0
    else:
        pass

    # return end date of the year-month
    if leap_year_flag == 1 and month == 2:
        return 29
    elif leap_year_flag == 1 and month != 2:
        return end_dates[month]
    else:
        return end_dates[month]


times = []
for i in range(int(day), int(last_day_month(year, month)) + 1):
    times.append(f'{i}')
