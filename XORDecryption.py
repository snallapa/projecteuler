from string import ascii_lowercase
import itertools
f = open('cipher.txt', 'r')

def decrypt(characters):
	for a in ascii_lowercase:
		for b in ascii_lowercase:
			for c in ascii_lowercase:
				newcharacters = []
				for i in xrange(0, len(characters)):
					xorcharacter = a
					if i % 3 == 0:
						xorcharacter = a
					elif i % 3 == 1:
						xorcharacter = b
					else:
						xorcharacter = c
					newcharacters.append(characters[i] ^ ord(xorcharacter))
				decrypted = ''.join(chr(i) for i in newcharacters)
				if " and " in decrypted:
					return newcharacters

characters = []
for line in f:
	for number in line.split(","):
		characters.append(int(number.strip()))
print sum((decrypt(characters)))