# latitude_test

Here you can provide any fixed width file in "Windows-1252" format, the code will convert it into CSV.

To run it with Docker:
docker build -t latitude/parser:1.0 .
docker run -ti --name parser latitude/parser:1.0

It will run the test cases written here. Input files it will pick from "fixed-width/input" folder
And Output will save in "fixed-width/output" folder.

To run it with main.py:
cd fixed-width
python main.py <input-file-path>

Output will provide in "output.csv" in "fixed-width/output" folder
