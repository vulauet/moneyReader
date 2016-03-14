# import MySQLdb
import mysql.connector as mariadb

# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
db = mariadb.connect(user = "vula", password = "mat.khau.cua.vula", database = "vudb")
cursor = db.cursor()

data = open('./rate/USD.txt', 'r').read()
data = data.split('\n')
insertNewRate = "INSERT INTO rate_exchange (base_banknote_id, rate_banknote_id, rate) VALUES(%s, %s, %s);"
for i in range(0,len(data),3):
	value = (data[i], data[i+1], data[i+2])
	cursor.execute(insertNewRate, value)
db.commit()
db.close()