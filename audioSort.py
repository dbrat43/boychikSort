import os, os.path
import re
from bs4 import BeautifulSoup

with open ("new boychiks chat.html") as file:
	soup = BeautifulSoup(file, 'html.parser')

	audio_tag = str(soup.find_all('audio'))

	audioArray = []

	# add audio files to array
	for audioLink in soup.find_all('a'):
		if re.match(r"messages/audio/", audioLink.get('href').encode('utf-8')):
			temp = audioLink.get('href').encode('utf-8')
			oldFileName = temp.split('/')[2]
			audioArray.append(oldFileName)

 	
 	# path to audio files	
	directory = os.listdir("C:\\Users\\Daniel\\Desktop\\facebook-danieljosephb\\messages\\audio")
	

	for file_x in audioArray:

		oldFilePrefix = file_x.split('.')[0]
		oldFileSuffix = file_x.split('.')[1]

		newFilePrefix = 1
		
		for file_y in directory:

			# newFilePrefix += 1
			

	 		# rename files in numerical order
			if file_y.startswith(oldFilePrefix):

				print oldFilePrefix
				newFileName = str(newFilePrefix) + "." + oldFileSuffix
				print newFileName
				newFilePrefix += 1
				# numString = newFileName.split('.')[0]
				# print numString
				# newFilePrefix = chr(ord(numString) + 1)
				# print newFilePrefix
				# print newFileName
			# os.rename("C:\\Users\\Daniel\\Desktop\\facebook-danieljosephb\\messages\\audio\\" + file, "C:\\Users\\Daniel\\Desktop\\facebook-danieljosephb\\messages\\audio\\" + newFileName)


file.close()

# # oldest file is 10205825239851378.mp4