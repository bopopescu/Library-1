import mysql.connector
from mysql.connector import errorcode

config={'user': 'root',
        'password':'kennedy',
        'host':'127.0.0.1',
        'database':'Library'}
try:
    cnx = mysql.connector.connect(**config)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid Username or Password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
