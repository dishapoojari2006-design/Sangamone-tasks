
start = 3
end = 20
for table in range(start, end + 1):

    print("Table of", table)
    for i in range(1, 11):
        print(table, "*", i, "=", table * i)
    print()