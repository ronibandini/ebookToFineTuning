# eBook to fine tunning
# Roni Bandini, August 2024
# MIT License

import sys

lastWasDialog=0
previousAnswer=""
howManyLines=300
counter=0

if len(sys.argv)<2:
	print("Use example: ebookToFineTuning.py shakespeare.txt \"John is a great writer\"")
	exit(1)

fileName 	= sys.argv[1]
systemDetails	= sys.argv[2]

fileName=fileName.replace(".txt", "")

myFile = open(fileName+".jsonl", "w", encoding="utf-8")

print("eBook to openAI Fine Tuning JsonL")
print("Roni Bandini, Agosto 2024")
	

print("Entry file: "+fileName)
with open(fileName+'.txt', 'r', encoding="utf-8") as f:

	for linea in f:

		if linea[0]=="—" or linea[0]=="-":

			lineaParseada=linea.replace('—', '')
			lineaParseada=linea.replace('- ', '')
			lineaParseada=linea.replace('-', '')
			lineaParseada=lineaParseada.replace('\n', '')


			if lastWasDialog==1:

				myExportLine="{\"messages\": [{\"role\": \"system\", \"content\": \""+sys.argv[2]+".\"}, {\"role\": \"user\", \"content\": \""+previousAnswer+"\"}, {\"role\": \"assistant\", \"content\": \""+lineaParseada+"\"}]}"

				myFile.write(myExportLine+'\n')
				#print(str(counter)+":"+myExportLine)
				print(str(counter)+" ...")

				counter=counter+1
			
			else:
				#print("Start: "+linea)
				lastWasDialog=1

			previousAnswer=lineaParseada


			if counter==howManyLines:
				print("Limit reached...")
				break
		else:
			lastWasDialog=0

f.close()
print("")
print("You can upload "+fileName+".jsonl to https://platform.openai.com/finetune/")




