import csv
import re

def db_search(phrase):
	#specific = [] #for results that start the with the given phrase
	#non_specific = [] #for results where the phrase occurs anywhere
	
	results = {
		"specific": [],
		"non_specific":[]
	}
	
	db = csv.reader(open('urhobo-dictionary.csv', 'r', encoding="utf-8"), delimiter=',')
	
	for line in db:
		if re.search(fr"^{phrase}", line[2], flags=re.I)is not None:
			results["specific"].append(line)
		elif phrase in line[2] and line not in results["specific"]:
			results["non_specific"].append(line)

	return results