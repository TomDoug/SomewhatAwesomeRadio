import pexpect, time
class mpg:
	def __init__(self):
		print "init"	
		self.c = pexpect.spawn('mpg123')
	def play(self, path):
		new = path.replace(" ", "\\ ")
		self.c = pexpect.spawn('mpg123 -C %s' % new)
		print 'mpg123 -C %s' % new
	def pause(self):
		self.c.sendline(" ")
	def stop(self):
		self.c.sendline("q")
#c.sendline("v")
#c.sendline('v')
#c.sendline('v')
#ptime = ""
#i = 0
#while c.isalive():
#	c.expect_exact('Time:')
#	print c.read(8)
#	i+=1
#	if i == 40:
		#stop()
	
