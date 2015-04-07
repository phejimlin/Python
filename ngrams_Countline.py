# -*- coding: utf-8 -*-

import sys
from nltk.util import ngrams
import string
from string import maketrans
from operator import itemgetter, attrgetter, methodcaller
#File_text=sys.argv[1]
#N_grams=int(sys.argv[2])

#print File_text,N_grams

#the line counter
line_counter=0
model={}

infile = file('apple.txt',"r")
while True:
	line_counter+=1
	#print line_counter

	try:
		File_read_line=infile.readline()
		File_read_line=File_read_line.lower() 		#change all to small
		out_remove_punctuation = File_read_line.translate(string.maketrans("",""), string.punctuation) 		#remove punction

		N_grams_read=ngrams(out_remove_punctuation.split(),2)

		for N_grams_word in N_grams_read:
			#print N_grams_word 

			if N_grams_word in model:
				model[N_grams_word][0]+=1 #有在model裏 出現過 總共次數加一
				model[N_grams_word].append(line_counter) 

			else:
				model[N_grams_word]=[1, line_counter] #如果沒在model裏 就是第一次出現

	except IOError:
		print "Error: can\'t find file or read data"
		break
	else:
		if(File_read_line==""):
			break
infile.close()

model=sorted(model.items(), key=itemgetter(1),reverse=True)
#print N_grams_word
for i in range(5):
	print model[i]