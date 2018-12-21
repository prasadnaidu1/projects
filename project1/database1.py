
import cx_Oracle
connection=cx_Oracle.connect("system","tiger","localhost:1521\ex")
cursor=connection.cursor()
cursor=cursor.execute("select*from emp")
lst=cursor.fetchall()
for row in lst:
    print(row)
connection.close()