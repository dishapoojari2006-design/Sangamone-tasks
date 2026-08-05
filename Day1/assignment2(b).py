
start = int(input("Enter the first number:"))
end = int(input("Enter the first number:"))
for table in range(start, end + 1):

    print("Table of", table)
    for i in range(1, 11):
        print(table, "*", i, "=", table * i)
    print()