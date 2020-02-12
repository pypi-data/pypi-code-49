import pyAesCrypt, os, getpass
import simplejson as json
from pathlib import Path
from datetime import datetime
from ast import literal_eval

from tkinter import font
from tkinter import *

class TextEditor:
	def __init__(self, name):
		self.name = name
		self.content_text_editor = ""

	def start(self):
		root = Tk()
		helv36 = font.Font(family="Helvetica",size=16,weight="bold")
		self.text = Text(root, bg='papaya whip', fg='saddle brown', height=30, width=100, wrap=WORD, yscrollcommand=True, font=helv36)
		self.text.pack()
		b = Button(root, fg='black', bg='khaki', activeforeground='black', activebackground='khaki', text="Save {}".format(self.name), command=self.retrive_text)
		b.pack()
		mainloop()

	def retrive_text(self):
		self.content_text_editor = self.text.get("1.0",'end-1c')

class Diary:
	def __init__(self, owner, password):
		self.owner = owner
		self.password = password
		self.path_name = Path("{}.json".format(owner))
		self.name_file = "{}.json".format(owner)
		self.bufferSize = 64 * 1024

	def access(self):
		if self.diary_exist():
			if self.decrypt_part('password')[0]:
				self.login = True
				action = ""
				while action == "":
					action = input("What you wanna do? (read, write, exit): ")

					if action == "write":
						self.write_to_diary()
					elif action == "read":
						if len(self.diary_content['dates']) > 0:
							self.show_days()
							selected_page = input("\n\nNow select tha page number: ")
							while not selected_page.isdigit():
								selected_page = input("\n\nNow select tha page number: ")
							self.read_day(int(selected_page))
						else:
							print("No elements in your diary, you can't read empty pages")
					elif action == "exit":
						break

					action = ""
				return True
			else:
				print("Ops! I don't know who you are... So go away")
				self.login = False
				return False

	def write_to_diary(self):
		print("For first write the details of the day, no limits\n\nTo save text click the button you see at bottom, if not pressed text will be seen as empty so will not added to diary.")
		day_details = ""
		while day_details == "":
			day_details = input("To continue write something: ")
		my_day_details = TextEditor('details')
		my_day_details.start()
		self.day_details = my_day_details.content_text_editor

		print("Now, for privacy set the summary of this day, untill now obviously.\n\nSummary will not be encripted so everyone can see this plain text but details will be encripted so only you can see everything.\n\nLike before, write the summary and press the Save button you see at bottom.")
		summary_text = ""
		while summary_text == "":
			summary_text = input("To continue write something: ")
		my_summary = TextEditor('summary')
		my_summary.start()
		self.summary_text = my_summary.content_text_editor

		with open('content_day.txt', 'w') as write_day:
			write_day.write(self.day_details)

		with open('summary_day.txt', 'w') as summary_Day:
			summary_Day.write(self.summary_text)

		self.add_to_diary()


	def diary_exist(self):
		if not self.path_name.is_file():
			create_one = input("Wanna create new diary? (y/n)")
			while create_one == "":
				create_one = input("Wanna create new diary? (y/n)")
			if create_one.lower() == "y" or create_one.lower() == "yes":
				with open(self.path_name, "w") as file_write:
					self.diary_json = {'owner':self.owner, 'dates':list()}
					self.encrypt_part(self.password)
					self.diary_content = {'owner':self.owner, 'dates':list(), 'password':str(self.encripted_file)}
					json.dump({'owner':self.owner, 'dates':list(), 'password':str(self.encripted_file)}, file_write)
				return True
			return False
		else:
			with open(self.name_file, 'r') as diary:
				self.diary_content = json.loads(diary.read())
		return True

	def add_to_diary(self):
		now = datetime.now()
		
		pyAesCrypt.encryptFile("content_day.txt", "content_day.aes", self.password, self.bufferSize)

		with open('content_day.aes', "rb") as content_day:
			my_day = content_day.read()

		with open('summary_day.txt', "r") as summary_txt:
			my_summary = summary_txt.read()

		if len(self.diary_content['dates']) == 0:
			self.diary_content['dates'].append({'{}'.format(now.strftime('%d-%b-%Y')):{'summary':[{'time':now.strftime('%I:%M:%S %p'), 'text':my_summary}], 'day_content':[{'time':now.strftime('%I:%M:%S %p'), 'text':"{}".format(my_day)}]}})
		else:
			found = False
			all_days = self.diary_content['dates']
			for day in all_days:
				if now.strftime('%d-%b-%Y') in day:
					day["{}".format(now.strftime('%d-%b-%Y'))]['summary'].append({'time':now.strftime('%I:%M:%S %p'), 'text':my_summary})
					day["{}".format(now.strftime('%d-%b-%Y'))]['day_content'].append({'time':now.strftime('%I:%M:%S %p'), 'text':"{}".format(my_day)})
					found = True
					break

			if found == False:
				self.diary_content['dates'].append({'{}'.format(now.strftime('%d-%b-%Y')):{'summary':[{'time':now.strftime('%I:%M:%S %p'), 'text':my_summary}], 'day_content':[{'time':now.strftime('%I:%M:%S %p'), 'text':"{}".format(my_day)}]}})
			
		os.remove("content_day.txt")
		os.remove("content_day.aes")
		os.remove("summary_day.txt")
		
		with open('{}'.format(self.name_file), "w") as write_json:
			json.dump(self.diary_content, write_json)

	def show_days(self):
		tmp_diary = self.diary_content['dates']
		self.diary_days = list()
		for pos, single_day_j in enumerate(tmp_diary):
			day = list(single_day_j.keys())[0]
			self.diary_days.append(list(single_day_j.keys())[0])
			print("\n\nPage {}, day {}".format(pos, day))
			for contents in single_day_j[day]['summary']:
				print("\n\tUpdate at {}, summary is\n\t\t{}".format(contents['time'], contents['text'].replace("\n", "\n\t\t")))
			

	def read_day(self, selected_day):
		tmp_diary = self.diary_content['dates']
		all_days = list()
		for pos, single_day_j in enumerate(tmp_diary):
			if pos == selected_day:
				day = list(single_day_j.keys())[0]
				print("\n\nPage {}, day {}".format(pos, day))
				for index, contents in enumerate(single_day_j[day]['day_content']):
					decr_txt = self.decrypt_specific(contents['text'])
					if decr_txt[0]:

						print("\n\tUpdate at {}, summary is\n\t\t{}\n\tContent of diary:\n\t\t{}\n\n".format(contents['time'], single_day_j[day]['summary'][index]['text'],self.decrypt_specific(contents['text'])[1].replace("\n", "\n\t\t")))
		

	def decrypt_specific(self, element):
		try:
			with open("nota_{}.aes".format('tmp_val'), 'wb') as ecnr_content:
				ecnr_content.write(literal_eval(element))

			pyAesCrypt.decryptFile("nota_{}.aes".format('tmp_val'), "nota_{}.txt".format('tmp_val'), self.password, self.bufferSize)

			with open('nota_{}.txt'.format('tmp_val'), "r") as reading_file:
				original_content = reading_file.read()

			os.remove("nota_{}.txt".format('tmp_val'))
			os.remove("nota_{}.aes".format('tmp_val'))

			return (True, original_content)
		except Exception as e:
			os.remove("nota_{}.txt".format('tmp_val'))
			os.remove("nota_{}.aes".format('tmp_val'))
			return (False, e) 

	def decrypt_part(self, key_json):
		try:
			with open("nota_{}.aes".format(key_json), 'wb') as ecnr_content:
				ecnr_content.write(literal_eval(self.diary_content[key_json]))

			pyAesCrypt.decryptFile("nota_{}.aes".format(key_json), "{}.txt".format(key_json), self.password, self.bufferSize)

			with open('{}.txt'.format(key_json), "r") as reading_file:
				original_content = reading_file.read()

			os.remove("{}.txt".format(key_json))
			os.remove("nota_{}.aes".format(key_json))

			return (True, original_content)
		except Exception as e:
			return (False, '')

	def encrypt_part(self, txt):
		with open('part_of_diary.txt', 'w') as pw_file:
			pw_file.write(txt)

		pyAesCrypt.encryptFile("part_of_diary.txt", "part_of_diary.aes", self.password, self.bufferSize)

		with open('part_of_diary.aes', 'rb') as pw_enc:
			self.encripted_file = pw_enc.read()

		os.remove('part_of_diary.txt')
		os.remove('part_of_diary.aes')

def main():
	diary_name = ""
	while diary_name == "":
		diary_name = input("Diary name: ").lower()

	password = ""
	while password == "":
		password = getpass.getpass("Diary password: ")

	my_diary = Diary(diary_name,password)

	my_diary.access()

if __name__ == '__main__':
	main()



