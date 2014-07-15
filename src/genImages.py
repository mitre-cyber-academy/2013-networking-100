from PIL import Image, ImageDraw, ImageFont
import os
import math
import uuid
import random

def main():
	flag = 'MCA-53C12E73'
	font = ImageFont.truetype(
		'/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf',
		24)
	alphabet = [chr(i) for i in range(33, 127)]
	#print out the numbers via the hexagonal sequence:
	# h_n = 2*n^2 - n 
	#Get the length of the string so we know how much garbage to give
	# out:
	flagLen = len(flag)
	#If we're using a square matrix, get the rounded-up square root of
	# the length, then fill that
	sideLen = int(math.ceil(math.sqrt(hexNum(flagLen + 1))))

	maxX = maxY = -1
	for char in alphabet:
		currX, currY = font.getsize(char)
		if(currX > maxX):
			maxX = currX
		if(currY > maxY):
			maxY = currY
	size = (maxX, maxY)

	currHexN = 1
	imgNameFile = open('fNameFile.txt', 'w')
	print sideLen
	for i in range(sideLen):
		currFNameArr = []
		for j in range(sideLen):
			count = i * sideLen + j + 1

			fName = str(uuid.uuid4()) + '.png'
			currImg = Image.new('L', size, (0xFF))
			draw = ImageDraw.Draw(currImg)
			if count == hexNum(currHexN) and currHexN - 1 < flagLen:
				#Create an image of the current index
				# of the flag
				currChr = flag[currHexN - 1]
				#Increment the current index
				currHexN += 1
			else:
				#Otherwise, draw a random character:
				currChr = random.choice(alphabet)
			draw.text((0,0), currChr, font=font)
			currImg.save(os.path.join('img', fName))
			imgNameFile.write(fName + ', ')
		imgNameFile.write('\n')

def hexNum(n):
	return 2 * n ** 2 - n

if __name__ == '__main__':
	main()
