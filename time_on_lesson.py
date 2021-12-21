from datetime import datetime
hour = datetime.now().hour
minute = datetime.now().minute
def lesson():
    if hour <= 8 and minute < 20:
        return 0
    elif hour ==8 and minute <= 59:
        return [1, 10]
    elif hour ==9 and minute <= 5:
        return [1, 10]
    elif hour == 9 and 10 <= minute <= 55:
        return [2, 15]
    elif hour == 10 and 10 <= minute <= 55:
        return [3, 15]
    elif hour == 11 and 10 <= minute <= 55:
        return [4, 15]
    elif hour == 12 and 10 <= minute <= 55:
        return [5, 5]
    elif hour == 13 and minute <= 45:
        return [6, 5]
    elif hour == 13  and minute>= 50:
        return [7, ]
    elif hour == 14 and minute <= 35:
        return [7, ]
    elif hour < 14:
        return [0, 10] if hour < 10 else ([0, 15] if 10 <hour< 13 else [0, 5])
    return ['в это время ты дома']


def left(x):
    if x[0] == 'в это время ты дома':
        return 'в это время ты дома'
    if x[0] == 1:
        return f' до конца урока осталось {65 - minute} минут'
    elif x[0] in [2, 3, 4, 5]:
        return f' до конца урока осталось {55 - minute} минут'
    elif x[0] == 6:
        return f' до конца урока осталось {45 - minute} минут'
    elif x[0] == 7 and hour == 13:
        return f' до конца урока осталось {95 - minute} минут'
    elif x[0] == 7 and hour == 14:
        return f' до конца урока осталось {35 - minute} минут'
    else:
        if x[1]==10:
            return f'сейчас у тебя перемена и осталось {x[1] - minute} минут до звонка'
        elif x[1] == 15:
            return f'сейчас у тебя перемена и осталось {x[1]  - (60 - minute if minute>55 else minute)} минут до звонка'
        elif x[1] == 5 and x[0]==5:
            return f'сейчас у тебя перемена и осталось {x[1]*12 - minute} минут до звонка'
        return f'до урока осталось {x[1] * 10 - minute}'

a = left(lesson())

