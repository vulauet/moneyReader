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


PORT_NUMBER = 12055

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	trademark_path = pjoin(curdir, str(datetime.now().microsecond) + ".jpg")

	#Handler for the GET requests
	def do_GET(self):
		# self.send_response(200)
		# self.send_header('Content-type','text/html')
		# self.end_headers()
		# # Send the html message
		# self.wfile.write("Hello World !")
		if self.path == '/USDVND':
			# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
			db = MySQLdb.connect(user="vula", password="mat.khau.cua.vu", database="vudb")
			cursor = db.cursor()
			query = "SELECT rate FROM rate_exchange WHERE base_banknote_id = 150 AND rate_banknote_id = 154;"
			cursor.execute(query)
			result = cursor.fetchone()
			dic = {}
			dic['USD - VND'] = float(result[0])
			print dic
			db.close()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(json.dumps(dic))

		elif self.path == '/USD':
			# db = MySQLdb.connect("localhost", "root", "toor", "banknote")
			db = MySQLdb.connect(user="vula", password="mat.khau.cua.vu", database="vudb")
			cursor = db.cursor()
			cursor.execute("SELECT rate_banknote_id, rate FROM rate_exchange WHERE base_banknote_id = 150;")
			rate = cursor.fetchall()
			cursor.execute("SELECT banknote_code FROM banknote")
			code = cursor.fetchall()

			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			dic = {}
			for i in range(168):
				dic['USD' + code[i][0]] = float(rate[i][1])
			self.wfile.write(json.dumps(dic))
		return

	def do_POST(self):
		if self.path == '/trademark':
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],})
			filename = form['file'].filename
			data = form['file'].file.read()
			with open(self.trademark_path, "wb") as fh:
				fh.write(data)
			self.send_response(200)

		elif self.path == '/moneyReader/':
			form = cgi.FieldStorage(
				fp=self.rfile,
				headers=self.headers,
				environ={'REQUEST_METHOD':'POST', 'CONTENT_TYPE':self.headers['Content-Type'],})


		return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

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