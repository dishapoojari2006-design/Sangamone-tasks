def quiz1(fname):
    countries = []
    capitals = []
    responses = []
    marks = []

    f1 = open(fname, "r")

    for i in range(0, 10, 1):
        s1 = f1.readline().strip()
        list1 = s1.split(",")

        countries.append(list1[0])
        capitals.append(list1[1])

    for i in range(0, 10, 1):
        print("What is the capital of", countries[i])
        responses.append(input())

    for i in range(0, 10, 1):
        if responses[i] == capitals[i]:
            marks.append(10)
        else:
            marks.append(0)

    print("Marks:", marks)

    total = sum(marks)
    print("Total Marks:", total)

    for i in range(0, 10, 1):
        if marks[i] == 0:
            print("What is the capital of", countries[i])
            print("Correct Answer:", capitals[i])


quiz1("GK1.txt")