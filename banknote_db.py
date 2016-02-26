import MySQLdb

# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
db = MySQLdb.connect("localhost", "vula", "mat.khau.cua.vula", "vudb")
cursor = db.cursor()

data = open('banknote.txt', 'r').read()
data = data.split('\n')
query = "INSERT INTO banknote (banknote_code, banknote_name) VALUES(%s, %s);"
for i in range(0,336,2):
 	value = (str(data[i]), str(data[i+1]))
	cursor.execute(query, value)
	# cursor.close()
	# cursor = db.cursor()

data = open('country.txt', 'r').read()
data = data.split('\n')
query = "INSERT INTO country (country_code, country_name) VALUES(%s, %s);"
for i in range(246):
 	value = (str(data[i]), str(data[i+246]))
	cursor.execute(query, value)
	# cursor.close()
	# cursor = db.cursor()

data = open('country_banknote.txt', 'r').read()
data = data.split('\n')
getCountryID = "SELECT country_id FROM country WHERE country_code = \'%s\';"
getBanknoteID = "SELECT banknote_id FROM banknote WHERE banknote_code = \'%s\';"
insertCountryBanknote = "INSERT INTO banknote_country (banknote_id, country_id) VALUES(%s, %s);"
for i in range(246):
	cursor.execute(getCountryID % str(data[i]))
	countryID = cursor.fetchone()
	cursor.execute(getBanknoteID % str(data[i+246]))
	banknoteID = cursor.fetchone()
	if (banknoteID):
		value = (banknoteID[0], countryID[0])
		cursor.execute(insertCountryBanknote, value)
	# cursor.close()
	# cursor = db.cursor()

data = open('./rate/USD.txt', 'r').read()
data = data.split('\n')
getBanknoteID = "SELECT banknote_id FROM banknote WHERE banknote_code = \'%s\';"
insertNewRate = "INSERT INTO rate_exchange (base_banknote_id, rate_banknote_id, rate) VALUES(%s, %s, %s);"
for i in range(0,504,3):
	cursor.execute(getBanknoteID % str(data[i]))
	baseID = cursor.fetchone()
	cursor.execute(getBanknoteID % str(data[i+1]))
	rateID = cursor.fetchone()
	value = (baseID, rateID, data[i+2])
	cursor.execute(insertNewRate, value)
db.commit()
db.close()