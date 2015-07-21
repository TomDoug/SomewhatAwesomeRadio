from glob import iglob
import shutil
import os

class Main():
	def start(self):
	

		PATH = r'C:\Users\Matt\Desktop\Desktop\Radio 628'

		destination = open('everything.mp3', 'wb')
		for filename in iglob(os.path.join(PATH, '*.mp3')):
			print filename
			if filename == 'C:\Users\Matt\Desktop\Desktop\Radio 628\everything.mp3':
				print 'nope'
			else:
		    		shutil.copyfileobj(open(filename, 'rb'), destination)
		destination.close()

