import MySQLdb

db = MySQLdb.connect("localhost", "root", "toor", "banknote")
cursor = db.cursor()

cursor.execute("SELECT banknote_id, country_id FROM banknote_country;")
data = cursor.fetchall()

print data

db.close()