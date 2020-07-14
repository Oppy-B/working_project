from datetime import datetime
import psycopg2

name = ''
address = ''
phone_num = ''
date_in_1 = ''
date_out_1 = ''
check_in = ''
check_out = ''


def add_info():
    global name
    global address
    global phone_num
    global date_in_1
    global date_out_1
    conn = psycopg2.connect(dbname='postgres', user='postgres', password='computer', host='localhost', port='5432')
    cur = conn.cursor()
    query = '''INSERT INTO hotel(name, address, phone_num, booking_dates) VALUES(%s, %s , %s, daterange(%s, %s, '[]') );'''
    cur.execute(query, (name, address, phone_num, date_in_1, date_out_1))
    conn.commit()
    conn.close()


def print_deluxe_price():
    global check_in
    global check_out
    deluxe_per_night = 100
    no_of_days = (check_out - check_in).days
    print('Your total amount due is $%s' % (deluxe_per_night * no_of_days))


def check_deluxe_date(indate, outdate):
    db_conn = psycopg2.connect(dbname='postgres', user='postgres', password='computer', host='localhost', port='5432')
    cur = db_conn.cursor()

    query = '''SELECT hotel_can_make_bookings(daterange(%s,%s,'[]') );'''
    cur.execute(query, (indate, outdate))
    row = cur.fetchone()
    if row == (False,):
        print('This date is not available')
        enter_deluxe_date()
    else:
        print('This date is available')
        add_info()
        print_deluxe_price()
    db_conn.commit()
    db_conn.close()


def main():
    print('WELCOME TO INTERCONTINENTAL HOTEL')
    print('1. BOOK A ROOM')
    print('2. ORDER FOR BREAKFAST')

    b = int(input('\nENTER YOUR CHOICE : '))
    if b == 1:
        enter_data()

    print('CHOOSE A ROOM')
    print('1. DELUXE ')
    print('2. PENTHOUSE')
    a = int(input('\nENTER ROOM CATEGORY'))
    if a == 1:
        enter_deluxe_date()
    elif a == 2:
        enter_penthouse_date()


def enter_data():
    global name
    global address
    global phone_num
    name = input('Enter your name : ')
    address = input('Enter your address : ')
    phone_num = input('Enter your phone number : ')


def enter_deluxe_date():
    global date_in_1
    global date_out_1
    global check_in
    global check_out
    print('DELUXE ROOM')
    date_in = input('Enter check in date : ')
    date_out = input('Enter check out date : ')
    try:
        check_in = datetime.strptime(date_in, "%Y/%m/%d")
        check_out = datetime.strptime(date_out, "%Y/%m/%d")
        date_in_1 = check_in.strftime("%Y/%m/%d")
        date_out_1 = check_out.strftime("%Y/%m/%d")
        check_deluxe_date(date_in_1, date_out_1)
    except ValueError:
        print('Incorrect date format')
        enter_deluxe_date()


def enter_penthouse_date():
    print('PENTHOUSE')
    date_in = input('Enter check in date : ')
    date_out = input('Enter check out date : ')
    try:
        check_in = datetime.strptime(date_in, "%d/%m/%Y")
        check_out = datetime.strptime(date_out, "%d/%m/%Y")

    except ValueError:
        print('Incorrect date format')
        enter_penthouse_date()


main()
