# Writing to a Text file

with open("./sample.txt","w") as file:
    file.write("Hello, Sahil\n")
    file.write("Welcome to Data Scientist Trainee role at Neosoft.\n")

# Reading from a text file

with open("./sample.txt","r") as txt_file:
    print(txt_file.read())

# Writing to a csv file
import csv

data = [
    ["Name","Age","Role"],
    ["Sahil Patel",24,"Data Scientist Trainee"],
    ["Mihir",22,"Data Scientist Trainee"]
]

with open("Employees.csv","w",newline="") as csv_file:
    writer=csv.writer(csv_file)
    writer.writerows(data)

# Reading from a csv file
with open("Employees.csv","r") as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        print(row)

