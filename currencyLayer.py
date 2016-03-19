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
		print datetime.datetime.now()
		quotes = result['quotes']
		for key in quotes:
			cursor.execute('UPDATE exchange_rate SET rate = %s, last_update = %s WHERE base_banknote_code = %s AND rate_banknote_code = %s', (quotes[key], datetime.datetime.now(), key[:3], key[3:]))
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

# {"USDZWL": 322.355011, "USDGHS": 3.965018, "USDTWD": 33.228992, "USDIDR": 13390.0, "USDMUR": 35.999753, "USDNGN": 198.990005, "USDILS": 3.9038, "USDETB": 21.323999, "USDKMF": 445.118988, "USDBMD": 1.00005, "USDPGK": 3.0411, "USDKYD": 0.819493, "USDKHR": 4005.899902, "USDJMD": 121.160004, "USDSAR": 3.75025, "USDAUD": 1.381769, "USDGIP": 0.718021, "USDCHF": 0.98765, "USDMVR": 15.38017, "USDSVC": 8.727198, "USDXCD": 2.698182, "USDIMP": 0.71506, "USDXOF": 593.491943, "USDEUR": 0.904077, "USDTOP": 2.233452, "USDLVL": 0.62055, "USDSCR": 13.26095, "USDNOK": 8.603904, "USDRWF": 765.210022, "USDALL": 125.044502, "USDUZS": 2846.629883, "USDBTC": 0.00238, "USDSYP": 219.800995, "USDBTN": 68.724998, "USDISK": 128.615005, "USDDZD": 107.334999, "USDAZN": 1.56495, "USDMKD": 55.715038, "USDFJD": 2.13085, "USDGBP": 0.713878, "USDCRC": 534.219971, "USDVUV": 113.050003, "USDBZD": 1.995001, "USDPAB": 0.99792, "USDDKK": 6.746699, "USDIQD": 1107.099976, "USDERN": 16.179889, "USDSZL": 15.570061, "USDLBP": 1509.699951, "USDTZS": 2183.149902, "USDXPF": 107.968048, "USDMMK": 1239.250298, "USDLYD": 1.386997, "USDGEL": 2.477986, "USDHKD": 7.76715, "USDBSD": 0.9978, "USDKPW": 899.99988, "USDZMK": 5156.12571, "USDSHP": 0.717996, "USDJEP": 0.71508, "USDXAU": 0.000808, "USDBBD": 2.0, "USDIRR": 30192.000165, "USDDJF": 177.645004, "USDHRK": 6.89095, "USDVEF": 6.350338, "USDTHB": 35.675999, "USDXAG": 0.066028, "USDXAF": 593.491943, "USDLAK": 8111.399902, "USDARS": 15.43795, "USDRUB": 75.424497, "USDCZK": 24.466499, "USDBRL": 3.95675, "USDPYG": 5712.505536, "USDPHP": 47.589502, "USDRON": 4.0409, "USDQAR": 3.64135, "USDCOP": 3343.050049, "USDTMT": 3.5, "USDEGP": 7.831804, "USDZMW": 11.385028, "USDLKR": 143.990005, "USDLTL": 3.048697, "USDBAM": 1.76955, "USDGGP": 0.71506, "USDAOA": 158.774994, "USDTND": 2.02835, "USDPKR": 104.605003, "USDHUF": 281.589996, "USDBIF": 1537.199951, "USDMYR": 4.21215, "USDLSL": 15.569435, "USDXDR": 0.71945, "USDUAH": 27.083762, "USDSEK": 8.47195, "USDTTD": 6.51125, "USDAWG": 1.79, "USDCUP": 0.999981, "USDSRD": 4.000101, "USDKRW": 1236.150024, "USDGMD": 39.450001, "USDCLF": 0.0246, "USDCUC": 1.0, "USDNZD": 1.478787, "USDGTQ": 7.678501, "USDTRY": 2.926301, "USDMRO": 342.999547, "USDCLP": 690.554993, "USDFKP": 0.659699, "USDLRD": 84.660004, "USDUYU": 32.075001, "USDKZT": 349.289948, "USDHTG": 61.543098, "USDCDF": 921.999695, "USDBHD": 0.37701, "USDMGA": 3210.949951, "USDRSD": 111.815002, "USDUSD": 1.0, "USDMAD": 9.80235, "USDSBD": 8.137236, "USDOMR": 0.38505, "USDJPY": 112.817001, "USDTJS": 7.869604, "USDKES": 101.742996, "USDYER": 214.889999, "USDMZN": 49.099998, "USDMDL": 19.959999, "USDNAD": 15.56991, "USDHNL": 22.599001, "USDBGN": 1.76835, "USDAED": 3.67315, "USDGNF": 7634.549805, "USDEEK": 14.151024, "USDPEN": 3.550058, "USDCAD": 1.35398, "USDMWK": 749.554993, "USDCVE": 99.753998, "USDBOB": 6.869773, "USDKWD": 0.300497, "USDBWP": 11.19845, "USDGYD": 207.210007, "USDAMD": 491.700012, "USDMNT": 2035.497632, "USDJOD": 0.709497, "USDUGX": 3362.999846, "USDSOS": 609.950012, "USDSGD": 1.399202, "USDDOP": 45.720001, "USDSTD": 22165.5, "USDAFN": 68.250496, "USDBYR": 21660.0, "USDCNY": 6.536302, "USDSLL": 4077.999985, "USDZAR": 15.56715, "USDBND": 1.399598, "USDNIO": 28.141302, "USDVND": 22322.5, "USDANG": 1.789601, "USDKGS": 74.455498, "USDINR": 68.755447, "USDMOP": 8.00125, "USDWST": 2.598134, "USDMXN": 18.129749, "USDSDG": 6.100103, "USDBDT": 78.259453, "USDNPR": 109.959999, "USDPLN": 3.942046}
