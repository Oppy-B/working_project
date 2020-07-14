import psycopg2
from datetime import datetime


def check_deluxe_date(indate, outdate):
        db_conn= psycopg2.connect(dbname='postgres', user='postgres', password= 'computer', host='localhost', port='5432')
        cur = db_conn.cursor()

        query = '''SELECT hotel_can_make_bookings(daterange(%s, %s, '[]') );'''
        cur.execute(query,(indate,outdate))
        row = cur.fetchone()
        print(row)
        if row == (False,):
            print('This is false')
        else:
            print('this is true')   
        db_conn.commit()
        db_conn.close()

def input_data():
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
        input_data()

    

    
    


input_data()
    





