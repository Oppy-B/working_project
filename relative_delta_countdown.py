from dateutil import tz,parser
from datetime import datetime
from dateutil.relativedelta import relativedelta

def time_amount(time_unit: str, countdown_func: relativedelta) -> str:
    t = getattr(countdown_func, time_unit)
    return f'{t} {time_unit}' if t != 0 else ''
       

def main():
    now = datetime.now(tz = tz.tzlocal())
    PYCON_DATE = parser.parse('MAY 12, 2021 8:00AM')
    PYCON_DATE = PYCON_DATE.replace(tzinfo= tz.gettz("America/New_York"))
    countdown = relativedelta(PYCON_DATE, now)
    time_units = ['years', 'months', 'days', 'hours', 'minutes','seconds']
    output = (x for tu in time_units if (x := time_amount(tu, countdown)) )
    pycon_date_str = PYCON_DATE.strftime('%A, %B %d, %Y at %H:%M %p %Z')
    print('Pycon US 2021 will start on : %s' % (pycon_date_str) )
    print('Countdown to Pycon US 2021 : ', ','.join(output))

if __name__ == "__main__":    
    main()






