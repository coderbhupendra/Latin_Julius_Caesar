import urllib
import re
import os 
import string
from nltk import tokenize
from cltk.tokenize.sentence import TokenizeSentence

try:
	from bs4 import BeautifulSoup
except ImportError:
	from BeautifulSoup import BeautifulSoup
	

def scrap_doc():
	#scraping table
	regex = re.compile('[%s]' % re.escape(string.punctuation))
	
	tokenizer_latin = TokenizeSentence('latin')	
	directory="dataset/dbg"
	if not os.path.exists(directory):
			os.makedirs(directory)

	for i in range (1,9):
		url="http://sacred-texts.com/cla/jcsr/dbg"+str(i)+".htm"
		
		html = urllib.urlopen(url)
		soup = BeautifulSoup(html)

		
		#create text file
		target_e = open("dataset/dbg/dbg"+str(i)+"_eng.txt", 'w')
		target_l = open("dataset/dbg/dbg"+str(i)+"_lat.txt", 'w')

		#to remove <a></a>
		for tag in soup.find_all('a'):
			tag.replaceWith('')
		
		k=0
		for tr in soup.find_all('tr')[0:]:
			k=k+1
			tds = tr.find_all('td')
			col1=tds[0].text
			col2=tds[1].text
	
			col1_tok=tokenize.sent_tokenize(col1)
			#col2_tok=tokenize.sent_tokenize(col2)
			
			col2_tok=tokenizer_latin.tokenize_sentences(col2)

			no_sentences_eng=0
			#writing sentences to a file
			for l in range(len(col1_tok)):
				line=col1_tok[l]
				#line=regex.sub('', line).strip()
			
			
				if line!="":
					#line+='.'
					target_e.write((line.lower()).encode('utf-8'))
					target_e.write("\n")
					no_sentences_eng+=1
			
			no_sentences_lat=0
			for l in range(len(col2_tok)):
				line=col2_tok[l]
				#line=regex.sub('', line).strip()
			
			
				if line!="":
					#line+='.'
					target_l.write((line.lower()).encode('utf-8'))
					target_l.write("\n")
					no_sentences_lat+=1
			
			if no_sentences_eng!=no_sentences_lat:
				print ("wrong ",i,k," :",(no_sentences_eng)	,(no_sentences_lat)) 	



if __name__ == "__main__":
	scrap_doc()