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
	pass