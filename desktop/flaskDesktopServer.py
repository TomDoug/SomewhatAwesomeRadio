import pexpect
from flask import Flask
from flask import request
from flask import render_template
from threading import Thread
import pexpectWraper
import os
import id3reader
import sqlite3
from pprint import pprint
app = Flask(__name__)
mpgWraper = pexpectWraper.mpg()

path = ""
#songs = []
#songends = []


#pprint (songs)



############################
#Song List
@app.route('/songs')
def main():
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	cur.execute("SELECT Title FROM Songs ORDER BY Title ASC")
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += '<a href = "/play/' + str(i[0]) + '">' +  str(i[0]) + "</a></br>"
		except:
			print "That one is fucked up"
			print i
	return songString
	
@app.route('/pi/songs')
def pi_main():
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	cur.execute("SELECT Title FROM Songs ORDER BY Title ASC")
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += str(i[0]) + "<br>"
		except:
			print "That one is fucked up"
			print i
	return songString

###############################
#Sort by Artist

@app.route('/artist')
def artist():
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	cur.execute("SELECT DISTINCT Artist FROM Songs ORDER BY Artist ASC")
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += '<a href="/artist/' + str(i[0]) + '">' + str(i[0]) + "</a></br>"
		except:
			print "That one is fucked up"
			print i
	return songString

@app.route('/artist/<artist>')
def art(artist):
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	artist = artist.replace('%20', ' ')
	cur.execute("SELECT Title FROM Songs WHERE Artist LIKE '%s' ORDER BY Title ASC" % artist)
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += '<a href ="/play/' + str(i[0]) + '">' + str(i[0]) + "</a></br>"
		except:
			print "That one is fucked up"
			print i
	return songString
	


@app.route('/pi/artist')
def pi_artist():
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	cur.execute("SELECT DISTINCT Artist FROM Songs ORDER BY Artist ASC")
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += str(i[0]) + "<br>"
		except:
			print "That one is fucked up"
			print i
	return songString

@app.route('/pi/artist/<artist>')
def pi_art(artist):
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	artist = artist.replace('%20', ' ')
	cur.execute("SELECT Title FROM Songs WHERE Artist LIKE '%s' ORDER BY Title ASC" % artist)
	songs = cur.fetchall()
	songString = ""
	for i in songs:
		try:
			songString += '<a href ="/play/' + str(i[0]) + '">' + str(i[0]) + "</a></br>"
		except:
			print "That one is fucked up"
			print i
	return songString
	
	
	
	
###############################
#PLay pause stop
@app.route('/play/<song>')
def play(song):
	path = ""
	print song
	song = song.replace('%20', ' ')
	print song
	
	con= sqlite3.connect('songs.db')
	cur = con.cursor()
	cur.execute("SELECT Path FROM Songs WHERE Title LIKE '%s'" % song)
	songs = cur.fetchall()
	
	try:
		path = str(songs[0][0])
	except:
		pass

	if path:
		mpgWraper.play(path)
	else:
		print "ERROR"
	return "Playing"
@app.route('/songinfo/<song>')
def songinfo(song):	
	song = song.replace('%20', ' ')
	for i in songs:
		if i.lower().count(song.lower()) != 0:
			path = i
			print path
			break
	id3r = id3reader.Reader(path)
	return "Artist:" + str(id3r.getValue('performer')) + "Album:" + str(id3r.getValue('album')) + "Title:" + str(id3r.getValue('title'))
@app.route('/pause')
def pause():
    mpgWraper.pause()
    return "Pausing"
@app.route('/stop')
def stop():
    mpgWraper.stop()
    return "Stoping"
if __name__ == "__main__":
    app.debug=True
    app.run(port=80, host = "0.0.0.0")
