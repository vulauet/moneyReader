import requests
# import MySQLdb
import datetime
import time
import mysql.connector as mariadb

while True:
	# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
	db = mariadb.connect(user="vula", password="mat.khau.cua.vula", database="vudb")
	cursor = db.cursor()
	# resp = requests.get('http://128.199.160.37:12056/USD')
	resp = requests.get('http://www.apilayer.net/api/live?access_key=dfc96bdc236e9d58869bec44fd74d277')
	if resp.status_code != 200:
		raise ApiError('GET /tasks/ {}'.format(resp.status_code))
	result = resp.json()
	if result['success'] == True:
		quotes = result['quotes']
		for key in quotes:
			cursor.execute('UPDATE update_exchange_rate SET rate = %s, last_update = %s WHERE base_banknote_code = %s AND rate_banknote_code = %s', (quotes[key], datetime.datetime.now(), key[:3], key[3:]))
		db.commit()
		db.close()
	time.sleep(43200)
# data = open('banknote.txt', 'r').read()
# data = data.split('\n')
# data = data[::2]
# print data

# for d in data:
# resp = requests.get('http://www.apilayer.net/api/live?access_key=dfc96bdc236e9d58869bec44fd74d277')



# d = result['quotes']

# f = open('./rate/USD.txt', 'w')
# # f.write(str(d))
# for key, value in d.iteritems():
# 	f.write(key + " " + str(value) + "\n")
# f.close()
# with open('./rate/USD.txt', "w") as f:
	# f.write(result['quotes'])
	# with open('./rate/' + d + ".txt", "w") as f:
	# 	for key, value in body.iteritems():
	# 		print key + ": " + str(value) + "\n"
	# 		f.write(key + " " + value + "\n")
# print "\n\n"
# mainBody = data['quotes']
# for key in mainBody: print key + "\n"
# print str(len(mainBody)) + "\n"
# for key, value in mainBody.iteritems():
# 	print key + ": " + str(value) + "\n"
