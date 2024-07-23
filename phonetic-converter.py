import csv

soundmap = {
	"a":"a",
	"á":"a",
	"e":"e",
	"é":"e",
	"ẹ":"ɛ",
	"́i":"iː",
	"́í":"iː",
	"o":"ɒ",
	"ó":"ɒ",
	"ọ":"ɔ",
	"b":"b",
	"ch":"tʃ",
	"d":"d",
	"dj":"d͡ʒ",
	"f":"f",
	"g":"g",
	"gh":"ɣ",
	"h":"h",
	"j":"d͡ʒ",
	"k":"k",
	"kp":"kpʰ",
	"m":"n",
	"n":"n",
	"p":"p",
	"r":"ɻ",
	"rh":"ṛ",
	"s":"s",
	"sh":"ʃ",
	"t":"tʰ",
	"u":"ʊ",
	"ú":"ʊ",
	"v":"v",
	"vw":"β",
	"y":"j",
	"z":"z",
}
def txt_to_phon():
	
	arr = []
	
	db = csv.reader(open('urhobo-dictionary-test.csv', 'r'), delimiter=',')
	
	
	for line in db:
		translation = ""
		for i in range(len(line[0])):
			print(line)
			if i == len(line[0]) - 1:
				translation += soundmap[line[0][i].lower()]		
			elif line[0][i] == "c":
				translation += sound_map["ch"]
				i+=1
			elif line[0][i] == "d" and line[0][i+1] == "j":
				translation += soundmap["dj"]
				i+=1
			elif line[0][i] == "g" and line[0][i+1] == "h":
				translation += soundmap["gh"]
				i+=1
			elif line[0][i] == "k" and line[0][i+1] == "p":
				translation += soundmap["kp"]
				i+=1
			elif line[0][i] == "n" and line[0][i+1] == "y":
				translation += soundmap["ny"]
				i+=1
			elif line[0][i] == "r" and line[0][i+1] == "h":
				translation += soundmap["rh"]
				i+=1
			elif line[0][i] == "s" and line[0][i+1] == "h":
				translation += soundmap["sh"]
				i+=1
			elif line[0][i] == "v" and line[0][i+1] == "w":
				translation += soundmap["vw"]
				i+=1
			elif line[0][i] == "m" and line[0][i+1] == "w":
				translation += soundmap["mw"]
				i+=1
			elif soundmap[line[0][i]] is not None:
				translation += soundmap[line[0][i]]
			else:
				translation += f"{line[0][i]}"
			arr.append(translation)
	
	print(arr)

txt_to_phon()
