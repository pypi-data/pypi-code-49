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
			shutil.rmtree(TRASHCANFILES)
			shutil.rmtree(TRASHCANINFO)
		except OSError as e:
			print(f"System Error: {e}")

def main():
	print("Started empting trash can\n")
	trashcan = TrashCan()
	trashcan.empty()
	print("Finished empting trash can\n")

if __name__ == "__main__":
	main()
