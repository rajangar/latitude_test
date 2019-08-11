import json
import sys
import parser

class Main:
	""" Main class to parse json file and call Parser to dump CSV
	"""
	def __init__(self, args):
		self.parsed_json = self.parseSpecJSON()
		self.input_file = args[0]

	def run(self):
		""" Calling Parser to Parse and Dump CSV
		"""
		parseAndDumpCSV = parser.ParseAndDumpCSV(self.parsed_json, self.input_file)
		parseAndDumpCSV.parse()

	def parseSpecJSON(self):
		""" Parsing spec.json file
		"""
		with open('spec.json', 'r') as json_file:
    			json_string = json_file.read()
		parsed_json = json.loads(json_string)
		return parsed_json

if __name__ == '__main__':
	try:
		if sys.argv[1:] == []:
			print("Provide input file in command arguments")
			raise
		main = Main(sys.argv[1:])
		main.run()
	except Exception as e:
		print("An error occured, error = ", e)
