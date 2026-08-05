start = 3
end = 8
file = open("out1.txt", "w")
for table in range(start, end + 1):
    file.write("Table of " + str(table) + "\n")
    for i in range(1, 11):
        file.write(str(table) + " * " + str(i) + " = " + str(table * i) + "\n")

    file.write("\n")
file.close()
print("Output successfully written to out1.txt")