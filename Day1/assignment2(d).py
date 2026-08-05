file = open("in2.txt", "r")
line = file.readline()
values = line.split(",")
start = int(values[0])
end = int(values[1])
file.close()
for table in range(start, end + 1):
    print("Table of", table)
    for i in range(1, 11):
        print(table, "*", i, "=", table * i)
    print()