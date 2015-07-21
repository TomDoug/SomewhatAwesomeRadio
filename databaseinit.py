import sqlite3
import id3reader
import os
from os.path import expanduser

con = sqlite3.connect('songs.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Songs(Path TEXT NOT NULL UNIQUE, Title TEXT, Artist TEXT, Album Text, Genre TEXT, Filename TEXT)") 

print expanduser("~")
for (dirpath, dirname, filenames) in os.walk('D:\\Users\\TomDoug\\Music'):#os.walk(u'' + expanduser("~") + '/Music'):
	for i in filenames:
		if i.count(".mp3") != 0:
			path = dirpath + '\\' + i
			id3r = id3reader.Reader(path)
			#print path
			print (id3r.getValue('album'))
			try:
				song = (unicode(path), id3r.getValue('title'), id3r.getValue('performer'), id3r.getValue('album'), id3r.getValue('genre'), i)
				cur.execute('INSERT INTO Songs VALUES(?,?,?,?,?,?)', song)
			except:
				continue
con.commit()
