import csv

class GenerateFixedWidthFile:

	def generate(self):
		with open("input/windows_1252_1.txt", "r", encoding="cp1252") as input_fl:
			input_str = input_fl.read()
		with open("input/large.txt", "w", encoding="cp1252") as output_fl:
			for i in range(1000000):
				output_fl.write(input_str + "\n")

		with open("output/windows_1252_1.csv", "r") as input_fl:
			header = input_fl.readline()
			input_str = input_fl.readline()
			input_str_1 = input_fl.readline()
		with open("output/large.csv", "w", newline='') as output_fl:
			writer = csv.writer(output_fl)
			writer.writerow(header.rstrip().split(','))
			for i in range(1000000):
				writer.writerow(input_str.rstrip().split(','))
				writer.writerow(input_str_1.rstrip().split(','))

if __name__ == '__main__':
	GenerateFixedWidthFile().generate()
