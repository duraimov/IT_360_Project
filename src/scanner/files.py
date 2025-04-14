import os
import re

class FileOpener:

	file_name = ""

	def __init__(self, file_name):

		self.opened_file = None
		self.file_name = file_name
	
	def open_file(self):
		
		self.opened_file=open(self.file_name, "r")

	def read(self):
		return self.opened_file.read()

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

	def list_files(self):
		return (file for file in os.listdir(self.dirname) if os.path.isfile(os.path.join(self.dirname, file)))
	
	def list_datastreams(self):
		print('no esta bien')
		return

	def get_file_path(self, filename):
		filepath = os.path.join(self.dirname, filename)
		return filepath

	def get_file(self, file_name):
		filepath = os.path.join(self.dirname, file_name)
		if os.path.exists(filepath):
			return FileOpener(filepath)
		else:
			print(f'Error: {filepath} does not exist')
			return None
