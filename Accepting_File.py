


class FileOpener:

	file_name = ""

	def __init__(self, file_name):

		self.file_name = file_name
	

	
		
	def open_file(self):


		self.opened_file=open(self.file_name, "r")

	def close_file(self):

		self.opened_file.close()

		


		

		



		
	





	

	









# def readFile( fileName ):
#     try:
#       file = open( fileName, "r")
#     except IOError:
#       print ("There was an error reading file")
#       sys.exit()
#     file_text = file.read()
#     file.close()
#     return file_text

# fileName = input("what is your file name?")

# readFile(fileName)





