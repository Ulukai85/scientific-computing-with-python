# Course project: Build a Time Calculator Project

def parse_time(time, pm=False):
    # Return time of clock in minutes
    hours, minutes = time.split(':')
    return (int(hours) + 12 * pm) * 60 + int(minutes)

def get_weekday(weekday, days):
    # Return new weekday
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday',
                'friday', 'saturday', 'sunday']
    if weekday == '': return ''
    index = weekdays.index(weekday.lower())
    return weekdays[(index + days) % 7].capitalize()

def add_time(start, duration, weekday=''):
    start, pm_am = start.split()
    time_delta = parse_time(start, pm_am=='PM') + parse_time(duration)
    hours = time_delta // 60 % 12 or 12
    minutes = time_delta % 60
    days_passed = time_delta // (60 * 24)
    pm_am = ('PM' if time_delta / 60 % 24 > 12 else 'AM')
    new_time = f'{hours}:{minutes:02d} {pm_am}'
    if weekday:
        new_time += ', ' + get_weekday(weekday, days_passed)
    if days_passed:
        new_time += ' (next day)' if days_passed == 1 else f' ({days_passed} days later)'
    return new_time

add_time('2:59 AM', '24:00', 'saturDay')
add_time('8:16 PM', '466:02', 'tuesday')
