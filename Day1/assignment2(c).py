file=open("in1.txt","r")
start=int(file.readline())
end=int(file.readline())
file.close()
for table in range(start, end + 1):
    print("Table of", table)
    for i in range(1, 11):
        print(table, "*", i, "=", table * i)
    print()