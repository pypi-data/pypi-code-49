# Empty trash can
# /.local/share/Trash/ is the path to the 
# Trashcan in Ubuntu 18.04 replace it with your OS Trashcan path
import os
import shutil


TRASHCANFILES=f"{os.environ['HOME']}/.local/share/Trash/files/"
TRASHCANINFO=f"{os.environ['HOME']}/.local/share/Trash/info/"

class TrashCan():
	""" Define a trashcan with empty function"""
	def empty():
		""" Function to empty the trashcan """
		try:
			print("Start empting trash can\n")
			print("Removing files\n")
			shutil.rmtree(TRASHCANFILES)
			print("Removing information about files\n")
			shutil.rmtree(TRASHCANINFO)
			print("Finish empting trash can")
		except OSError as e:
			print(f"System Error: {e}")

def main():
	trashcan = TrashCan()
	trashcan.empty()
if __name__ == "__main__":
	main()
