import sublime, sublime_plugin

import socket
import sys
import json

import os

ip = "localhost"
port = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to INET socket
def Connect():	
	sock.connect((ip, port))

Connect()
 
class ClassRoomBroadcast(sublime_plugin.EventListener):
	def on_modified_async(this, view):
		curPos = view.sel()[0].a - 1
		curReg = sublime.Region(curPos)
		curChar = view.substr(curPos)
		curLine = view.substr(view.line(curReg));
		contents = view.substr(sublime.Region(0, view.size()));

		#Current document syntax
		language = os.path.splitext(os.path.basename(view.settings().get('syntax')))[0]
		language = language.lower()
		if language == "html":
			language = "htmlmixed"

		#Filename
		if view.file_name():
			filename = os.path.basename(view.file_name())
		else:
			filename = "untitled"
		
		#JSON packet to send
		packet = json.dumps({'lang' : language, 'file' : {'name' : filename, 'contents' : contents}});

		sock.send(packet.encode())
		print("Sent packet from file: " + filename) 