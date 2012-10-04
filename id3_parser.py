# id3 Tag parser
# Parses id3v2.2 and id2v2.3 tags
# By: Alexander Addy (ala47) and

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
class id3Parsed(mp3_file):
	"Given a mp3 file name, this will parse the id3 tag."""
	# put all the attributes the user might want into a main dictionary
	def __init__(self):
		self.attrs = {}
		#stuff

		self.ver = id3Ver(mp3_header)

		# get the encoding byte
		self.encoding = whichEncoding(encoding_byte)