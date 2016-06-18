import sublime, sublime_plugin

import socket
import sys

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
		sock.send(contents.encode())
		print("Sent packet")