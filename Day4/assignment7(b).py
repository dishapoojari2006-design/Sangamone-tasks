def quiz2(fname):
    questions = []
    answers = []
    responses = []
    marks = []

    f1 = open(fname, "r")

    for i in range(0, 9, 1):
        s1 = f1.readline().strip()
        list1 = s1.split("$$")

        questions.append(list1[0])
        answers.append(list1[1].strip())

 
    for i in range(0, 9, 1):
        print(questions[i])
        responses.append(input())

    for i in range(0, 9, 1):
        if responses[i] == answers[i]:
            marks.append(10)
        else:
            marks.append(0)

    print("Marks:", marks)

    total = sum(marks)
    print("Total Marks:", total)

    for i in range(0, 9, 1):
        if marks[i] == 0:
            print("Question:", questions[i])
            print("Correct Answer:", answers[i])


quiz2("GK2.txt")