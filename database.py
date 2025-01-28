import mysql.connector as sql
mycon = sql.connect(
        host = '127.0.0.1',
        user = "root",
        password = "abimbola",
        database = 'new_db' 

)
mycursor = mycon.cursor()
# mycursor.execute("CREATE DATABASE new_db")
# print('dtabase created')

mycursor.execute("CREATE TABLE staff(staff_id INT PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, password VARCHAR(20), date_created DATETIME DEFAULT CURRENT_TIMESTAMP)")
# print('Table created')

mycursor.execute('SHOW DATABASES')
for db in mycursor:
        print( db)

mycursor.execute("SHOW TABLES")
for table in mycursor:
        print(table)

mycursor.execute("ALTER TABLE staff ADD (gender VARCHAR(10), department VARCHAR (50))")
# print('column added')





