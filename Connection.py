from sqlite3 import Cursor, connect
import psycopg2

def table():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5433")

    cursor = conn.cursor() #making cursor and connecting it
    cursor.execute(''' create table employees(Name text, Id int, Age int);''') #creating the table

    print("Table Created!!!!")

    conn.commit() #to commit the changes
    conn.close() #closing the connection

def data():
    conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5433")

    cursor = conn.cursor() #making cursor and connecting it
    name = input('enter name: ')
    id = input('enter id: ')
    age = input('enter age: ')
    #cursor.execute(''' insert into employees(Name,Id,Age) values('sam',01,20);''') #inserting into the table
    query = '''insert into employees(Name,Id,Age) values(%s,%s,%s);''' #make user enter the values
    cursor.execute(query,(name,id,age)) #take values from the above query

    print("data added sucessfully!!!!")

    conn.commit() #to commit the changes
    conn.close() #closing the connection

data()

#def extract():
#    conn = psycopg2.connect(dbname="postgres",user="postgres",password="root",host="localhost",port="5433")
#    cursor = conn.cursor() #making cursor and connecting it
#    cursor.execute(''' select * from employees;''') #extracting from the table
#    print(cursor.fetchone()) #fetching the sql query values
#    print("values!!!!")
#    conn.commit() #to commit the changes
#    conn.close() #closing the connection
#extract()
