import re
import os.path

from PyPDF2 import PdfFileWriter, PdfFileReader

def words(text):
    pattern = re.compile(r"[^\s]+")
    non_alpha = re.compile(r"[^a-z]", re.IGNORECASE)
    for match in pattern.finditer(text):
        yield non_alpha.sub("", match.group()).lower()

def phrases(words):
	tuplesize = 7
	phrase = []
	for word in words:
		phrase.append(word)
		if len(phrase) > tuplesize:
			phrase.remove(phrase[0])
		if len(phrase) == tuplesize:
			yield tuple(phrase)

def readtext(filename):
	output = PdfFileWriter()
	input1 = PdfFileReader(open(filename, "rb"))

	# print how many pages input1 has:
	numpages = input1.getNumPages()
	print "File has %d pages." % numpages

	text = ""

	for i in range(numpages):
		text += (input1.getPage(i)).extractText()
	#	print "page %d" % i
	print "text collated!"
	return text

#look for preexisting text file
if not os.path.isfile('book.txt'):
	file = "ImmigrantSchoenhoffBK103.pdf"
	text = readtext( file )
	f = open('book.txt', 'w')
	f.write( text.encode('ascii', errors='backslashreplace') )
	f.close()
else:
	f = open('book.txt', 'r')
	text = f.read()
#print text

#print text[0:1000]

#Find names
namelist = ["Dr. Black", "Peturka", "Bahr", "glen", "oracle", "dan", "betty", "mike", "amy", "drebes", "charmain",
 "charmaine", "chuck", "pauline", "turner", "klaus", "ingrid", "annelise", "gerhard", "pat", "russell", "rolf", "phil",
 "greta", "schneider", "ken", "kathy", "ehlers", "glens", "bart", "jim", "karma", "allen", "lisa", "john", "stacey", 
 "mike", "gabi", "brit", "anneliese", "bill", "monica", "bob", "perryman" ]

for name in namelist:
	search = 0
	count = 0
	print name
	while search != -1:
		search = text.lower().find(name.lower(), search+1)
		count += 1
		print "..." + text[search-20:search+20] + "..."
#	print search

	print "count = %d" % count


counts = {}
#list(phrases(words(text)))
for phrase in phrases(words(text)):
	string = phrase
	#[0] + ' ' + phrase[1] + ' ' + phrase[2]
	if string in counts:
		counts[string] += 1
	else:
		counts[string] = 1

for i in counts.keys():
	if counts[i] > 1:
		s = ''
		for j in range(len(i)):
			s += i[j] + ' '
		print s, counts[i]

#for i in range(len(text)/20):
#	dupe = text.find(text[i*20:i*21], i*21)
#	if dupe != -1:
#		print i, dupe
#		print text[i*20:i*21]

print "complete"