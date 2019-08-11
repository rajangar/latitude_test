import csv

class ParseAndDumpCSV:
	""" Helping in parsing the file in Windows-1252 format with fixed width size
	And dump file in csv format
	"""

	def __init__(self, parsed_json, input_file):
		self.parsed_json = parsed_json
		self.input_file = input_file

	def parse(self):
		""" Here the actual parsing and dumping happen
		"""

		inputEncode = self.parsed_json['InputEncoding']
		try:
			input_fl = open(self.input_file, "r", encoding=inputEncode)
		except Exception as e:
			print("IO Error in input file", self.input_file, ", error = ", e)

		try:
			output_fl = open("output/output.csv", "w", encoding=self.parsed_json['OutputEncoding'], newline='')
		except Exception as e:
			print("IO Error while opening output file, error = ", e)

		writer = csv.writer(output_fl)

		if self.parsed_json['IncludeHeader'] == "True":
			columns = self.parsed_json['ColumnNames'].split(', ')
			writer.writerow(columns)

		offsets = self.parsed_json['Offsets'].split(',')

		total_width = 0
		for offset in offsets:
			total_width += int(offset)

		line_no = 0
		lines = []
		for input_line in input_fl:
			line_no += 1
			try:
				input_line = input_line.encode(inputEncode).decode(inputEncode).encode('utf-8').decode('utf-8').rstrip()
				if total_width != len(input_line):
					raise IndexError
				line = []
				length = 0
				for ind, offset in enumerate(offsets):
					line.append(input_line[length:length + int(offset)].strip())
					length = length + int(offset)
				if line_no % 2000 == 0:
					writer.writerows(lines)
					lines = []
				lines.append(line)

			except IndexError as e:
				print("Error in Line no", line_no, ", skipped, error = ", e)
				continue
			except Exception as e:
				print("Error in Line no", line_no, ", skipped, error = ", e)
				continue

		writer.writerows(lines)
			
		output_fl.close()
		input_fl.close()
