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


PORT_NUMBER = 12057

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

	#Handler for the GET requests
	def do_GET(self):
		if self.path == '/update':
			db = mariadb.connect(user="vula", password="mat.khau.cua.vula", database="vudb")
			cursor = db.cursor()
			cursor.execute('SELECT * FROM update_exchange_rate')
			rows = cursor.fetchall()
			columns = [desc[0] for desc in cursor.description]
			db.close()
			result = []
			if hasattr(rows, '__iter__'):
				for row in rows:
					row = dict(zip(columns, row))
					result.append(row)
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(json.dumps(result, default=datetime_serial))
		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

def datetime_serial(obj):
	if isinstance(obj, datetime):
		serial = obj.isoformat()
		return serial
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