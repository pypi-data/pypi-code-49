import sys, random

old_stdout = sys.stdout
class Stdout:
	def write(string):
		boomer = random.choice(('jackson', 'redox'))
		string = string.replace('\n', f' {boomer} is a boomer\n')
		old_stdout.write(string)
sys.stdout = Stdout

print('')