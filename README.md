# latitude_test

Here you can provide any fixed width file in "Windows-1252" format, the code will convert it into CSV.

-	To run it with Docker:
		docker build -t latitude/parser:1.0 .
		docker run -ti --name parser latitude/parser:1.0

	It will run the test cases written here. Input files it will pick from "fixed-width/input" folder
	And Output will save in "fixed-width/output" folder.

-	To run it with main.py:
		cd fixed-width
		python main.py <input-file-path>

	Output will provide in "output.csv" in "fixed-width/output" folder

-	Large file with 2 million rows test is added, to check it manually:

		python fixedgenerator.py #Will generate large.txt and large.csv for input and validation
		python main.py input/large.txt #Will produce output/output.csv and can be validated

-	Test cases will take little bit extra time (more than a minute) because of large file generation and parsing.
	I have tried to decrease that time by optimising the CSV writing as writing multiple rows at a time, which can
	be more optmised by increasing the memory capacity


-	Scope is limited to one file, but multiple files can be given as input and Celery workers with redis can be used
	to take one file each at a time
