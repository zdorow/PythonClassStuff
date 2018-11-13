import mysql.connector
mydb = mysql.connector.connect(
	host="picard.support.jamf.net",
	user="jamfsoftware",
	passwd="jamf1234",
	database="jamfsoftware"
)
mycursor = mydb.cursor()
mycursor.execute("select concat('alter table ', table_name, ' engine = innodb;') from information_schema.tables where table_schema = 'jamfsoftware' and engine = 'myisam' and table_name != 'downloadable_file_chunk_data'")
myresult = mycursor.fetchall()
for x in myresult:
	print(*x)
	mycursor.execute(*x)

mycursor.execute("select table_name,engine from information_schema.tables where tables.table_schema='jamfsoftware'")
result = mycursor.fetchall()
for x in result:
	print(x)

mydb.close()
