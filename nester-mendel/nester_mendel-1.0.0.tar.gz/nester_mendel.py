"""This is the "nester.py" module, which prints the contents of a list, including any additional nested lists."""

def printLol(theList):
	"""This function takes a positional argument called "theList", which is any Python list (of, possibly, nested lists).
	If the item is not a list, print the item to screen.  
	If it is a list, call the function printLol() again to recursively parse the nested list, printing each item on its own line"""
	for item in theList:
		if isinstance(item, list):
			printLol(item)
		else:
			print(item)