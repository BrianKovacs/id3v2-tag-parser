# id3 Tag parser
# Parses id3v2.2 and id2v2.3 tags
# By: Alexander Addy (ala47) and

# use these variables instead of the strings so that errors are easier to find
# and a spelling error doesn't happen
# DO NOT CHANGE THEM!
V2 = "v22"
V3 = "v23"
V4 = "v24"


def whichEncoding(encoding_byte):
	"""Returns the encoding type as a string.
		$00 - ISO-8859-1 (ASCII)
		$01 - UCS-2 (UTF-16 encoded Unicode with BOM), in ID3v2.2 and ID3v2.3
		$02 - UTF-16BE encoded Unicode without BOM, in ID3v2.4
		$03 - UTF-8 encoded Unicode, in ID3v2.4
		"""
	assert encoding_byte <= 3 and encoding_byte >= 0, TypeError("encoding unknown.")
	if encoding_byte == 0:
		pass
	elif encoding_byte == 1:
		pass
	elif encoding_byte == 2:
		pass
	elif encoding_byte == 3:
		pass

def frameSplit(mp3):
	"""Finds and returns the entirety of the next frame."""
	# maybe do this as a generator?
	# NYI
	pass

# assumes that the file is of type id3v2.2 or id3v2.3
class id3Parsed():
	"""Given a mp3 file name, this will parse the id3 tag."""
	# put all the attributes the user might want into a main dictionary
	def __init__(self, mp3_file):
		self.attrs = {}
		
		# open the file
		f = open(mp3_file, "rb")
		
		# get the the file cursor to the proper place (just after "ID3")
		for b in f:
			if(b == 'I'):
				temp = f.read(2)
				if(temp == 'D3'): break
				else: f.seek(-2, 1)

		# determine if the end of the file was reached
		if(f.read(1) == ''):# does this work? need to check
			f.close()
			raise TypeError("file does not contain id3v2 tag information")
		else: f.seek(-1, 1)

		self.ver, self.revision = self.id3Ver(f)

		# determine what the version is and react accordingly
		self.flags = {}
		if(self.ver == 2):
			self.ver = V2
			# NYI
			pass
		elif(self.ver == 3):
			self.ver = V3
			# NYI
			pass
		elif(self.ver == 4):
			self.ver = V4
			# NYI
			pass
		else:
			# NYI
			# raise some sort of error?
			f.close()
			pass
			
		# close the file
		f.close()
		
	def id3Ver(self, f):
		ver = f.read(1)
		rev = f.read(1)
		return ver, rev
		
	def flags2_2(self, flagbyte):
		if(flagbyte and 0b10000000): self.flags["synchro"] = True
		else: self.flags["synchro"] = False
		
		if(flagbyte and 0b01000000): self.flags["extended"] = True
		else: self.flags["extended"] = False
		
		if(flagbyte and 0b00100000): self.flags["experimental"] = True
		else: self.flags["experimental"] = False
		
	def flags2_3(self, flagbyte): # NYI
		pass
		
	def flags2_4(self, flagbyte): # NYI
		pass
		
	def tagSize(f): # NYI
		# 4 bytes where the MSB is zero and ignored
		# 4 * 0b0xxxxxxx, giving a total of 28 bits
		pass

if __name__ == "__main__":

	# place holder to test the file to be opened
	mp3_file = open("Kalimba.mp3", 'rb')
	print(mp3_file.read(3)) # should print 'ID3'