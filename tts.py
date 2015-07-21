import urllib2
import os
import mp3Test
from glob import iglob

class Main():

 def parseText(self, text):

  filelist = iglob("*.mp3")
  for i in filelist:
   os.remove(i)

  """ returns a list of sentences with less than 100 caracters """
  toSay = []
  punct = [',',':',';','.','?','!'] # punctuation
  words = text.split(' ')
  sentence = ''
  for w in words:
   if w[len(w)-1] in punct: # encountered a punctuation mark
    if (len(sentence)+len(w)+1 < 100): # is there enough space?
     sentence += ' '+w # add the word
     toSay.append(sentence.strip()) # save the sentence
    else:
     toSay.append(sentence.strip()) # save the sentence
     toSay.append(w.strip()) # save the word as a sentence
    sentence = '' # start another sentence
   else:
    if (len(sentence)+len(w)+1 < 100):   
     sentence += ' '+w # add the word
    else:
     toSay.append(sentence.strip()) # save the sentence
     sentence = w # start a new sentence
  if len(sentence) > 0:
   toSay.append(sentence.strip())
  return toSay

 def getText(self,theInput):

  #theInput = raw_input("What would you like me to say?")
  text = theInput

  print text
  toSay = self.parseText(text)

  google_translate_url = 'http://translate.google.com/translate_tts'
  opener = urllib2.build_opener()
  opener.addheaders = [('User-agent', 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)')]

  for i,sentence in enumerate(toSay):
   print i,len(sentence), sentence
   response = opener.open(google_translate_url+'?q='+sentence.replace(' ','%20')+'&tl=en')
   ofp = open(str(i)+'speech_google.mp3','wb')
   ofp.write(response.read())
   ofp.close()

  x = mp3Test.Main()
  print 'mp3 going'
  x.start()
