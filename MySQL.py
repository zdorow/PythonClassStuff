import mysql.connector
mydb = mysql.connector.connect(
	host="",
	user="",
	passwd="",
	database=""
)
mycursor = mydb.cursor()
mycursor.execute("select concat('alter table ', table_name, ' engine = innodb;') from information_schema.tables where table_schema = 'jamfsoftware' and engine = 'myisam'")
myresult = mycursor.fetchall()
for x in myresult:
	print(*x)
	mycursor.execute(*x)

mycursor.execute("select table_name,engine from information_schema.tables where tables.table_schema='jamfsoftware'")
result = mycursor.fetchall()
for x in result:
	print(x)

mydb.close()
