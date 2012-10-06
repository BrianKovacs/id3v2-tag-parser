# id3 Tag parser
# Parses id3v2.2 and id2v2.3 tags
# By: Alexander Addy (ala47) and

# use these variables instead of the strings so that errors are easier to find
# and a spelling error doesn't happen
# DO NOT CHANGE THEM!
V2 = "v22"
V3 = "v23"
V4 = "v24"

def id3Ver(mp3_header):
	pass
	
def whichEncoding(encoding_byte):
	"""Returns the encoding type as a string.
		$00 - ISO-8859-1 (ASCII)
		$01 - UCS-2 (UTF-16 encoded Unicode with BOM), in ID3v2.2 and ID3v2.3
		$02 - UTF-16BE encoded Unicode without BOM, in ID3v2.4
		$03 - UTF-8 encoded Unicode, in ID3v2.4
		"""
	pass

def frameSplit(mp3):
	"""Finds and returns the entirety of the next frame."""
	# maybe do this as a generator?
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

		self.ver = id3Ver(mp3_header)

		# get the encoding string
		self.encoding = whichEncoding(encoding_byte)
		
		# close the file
		f.close()
		

if __name__ == "__main__":
	mp3_file = open("Kalimba.mp3")
	
	print(str(mp3_file.read(20)))