import csv

# use .open to open files and return a file object
rows = []
numbersCalled = []
with open("data/SampleData0.csv") as file:
    csvreader = csv.reader(file)
    numbersCalled = next(csvreader) # first row is different than the others

    for row in csvreader:
        rows.append(row)
    # The readlines method returns all the lines in a file as a list. Each item of the list is a row of our CSV file. 
    # content = file.readlines() # this reads them in with the \n at the end of each line 
print(numbersCalled)
print(rows)
# This returned a _io.textIOWrapper object that can be read by the csv.reader
# The .next method returns the current row and moves to the next row. It will return the header the first time it's called, if there is one. 
# To Extract the rows/records, create an empty list and iterate through the csvreader ovject and append each row to the rows list. 
# After you are finished performing operations on your file, .close it if you didn't open it with "with". No  more operations can be performed after it is closed.

# numsCalled = content[:1]
# rows2 = content[1:]
# print(numsCalled)
# print(rows2)

# create a bingo boards with the sample data, each array of 5 values is a column. There are 5 columns per board. There is a blank row between each board