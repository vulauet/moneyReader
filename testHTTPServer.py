#!/usr/bin/python
from SocketServer import ThreadingMixIn
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import threading
from os import curdir
from os.path import join as pjoin
from datetime import datetime
import cgi
# import MySQLdb
import mysql.connector as mariadb
import json
import decimal

PORT_NUMBER = 12057

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		if self.path == '/update':
			db = mariadb.connect(user="vula", password="mat.khau.cua.vula", database="vudb")
			cursor = db.cursor()
			cursor.execute('SELECT base_banknote_code, rate_banknote_code, rate, image_link FROM exchange_rate')
			rows = cursor.fetchall()
			columns = [desc[0] for desc in cursor.description]
			rate = []
			if hasattr(rows, '__iter__'):
				for row in rows:
					row = dict(zip(columns, row))
					rate.append(row)

			cursor.execute('SELECT last_update FROM exchange_rate LIMIT 1')
			last_update = cursor.fetchone()
			db.close()
			result = {'rate': rate, 'last_update': last_update[0]}
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(json.dumps(result, default=object_serial))
		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def object_serial(obj):
	if isinstance(obj, datetime):
		serial = obj.isoformat()
		return serial
	elif isinstance(obj, decimal.Decimal):
		return float(obj)
	raise TypeError("Type not serializable")

if __name__ == '__main__':
	try:
		#Create a web server and define the handler to manage the
		#incoming request
		# server = HTTPServer(('', PORT_NUMBER), myHandler)
		server = ThreadedHTTPServer(('', PORT_NUMBER), myHandler)
		print 'Started httpserver on port ' , PORT_NUMBER
		
		#Wait forever for incoming htto requests
		server.serve_forever()

	except KeyboardInterrupt:
		print '^C received, shutting down the web server'
		server.socket.close()
