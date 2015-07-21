import pexpect
from flask import Flask
from flask import request
from flask import render_template
from threading import Thread
import pexpectWraper
import os
import id3reader

app = Flask(__name__)
mpgWraper = pexpectWraper.mpg()
path = "/home/tomdoug/Music/Brand New/Sic Transit Gloria...Glory Fades.mp3"
#path = "C:\Users\Matt\Music\Music\Brand New\Deja Entendu\02_Sic Transit Gloria...Glory Fades.mp3"
songs = []
songends = []
for (dirpath, dirname, filenames) in os.walk(os.getenv("HOME") + '/Music'):
	for i in filenames:
		if i.count(".mp3") != 0:
			path = dirpath + '/' + i
			songs.append(path)
			songends.append(i)

@app.route('/', methods = ['GET','POST'])
def main():

	if request.method == 'POST':
    		data = request.form.keys()[0]
        
    		print data
    		print type(data)
	songString = ""
	for i in songends:
		songString += i + "<br />"
	return songString
@app.route('/play/<song>')
def play(song):
	path = ""
	print song
	song = song.replace('%20', ' ')
	print song
	for i in songs:
		if i.lower().count(song.lower()) != 0:
			path = i
			print path
			break
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
    app.run(port=80)
