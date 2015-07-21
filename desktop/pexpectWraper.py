import pexpect

class mpg:
    def __init__(self):
        self.mpg = pexpect.spawn('mpg123')
	print "init"
    def play(self, path):
        new = path.replace(" ", "\ ")
        self.mpg = pexpect.spawn('mpg123 -C %s' % new)
	print "play"
    def pause(self):
        self.mpg.sendline(" ")
	print "pause"
    def stop(self):
        self.mpg.sendline("q")
	print "stop"
