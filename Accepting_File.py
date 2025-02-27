import os
import re

class FileOpener:

	file_name = ""

	def __init__(self, file_name):

		self.file_name = file_name
	
	def open_file(self):
		
		self.opened_file=open(self.file_name, "r")

	def print(self):
		
		print(self.opened_file.read())

	def close_file(self):

		self.opened_file.close()


	def search(self):
		keywords = "repeat"

		self.opened_file.read()
		


		for line in self.opened_file:

			matches = re.findall("test", keywords)
			print(matches)

			




class DirectoryHandler:
	dirname = ''

	def __init__(self, dirname):
		if os.path.exists(dirname):
			self.dirname = dirname
		else:
			print(f'Error: {dirname} does not exist')

	def list_files():
		print('no esta bien')
		return
	
	def list_datastreams():
		print('no esta bien')
		return
	
	def get_file(self, file_name):
		filepath = os.path.join(self.dirname, file_name)
		if os.path.exists(filepath):
			return FileOpener(filepath)
		else:
			print(f'Error: {filepath} does not exist')
			return None
