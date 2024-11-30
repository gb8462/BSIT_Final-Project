def code6():
    prelim = eval(input("Prelim Score: "))
    midterm = eval(input("Midterm Score: "))
    semi_finals = eval(input("Semi Final Score: "))
    finals = eval(input("Finals Score: "))
    quiz = eval(input("Quiz Score: "))
    project = eval(input("Project Score: "))

    Grade = (prelim * 0.15) + (midterm * 0.15) + (semi_finals * 0.15) + (finals * 0.15) + (quiz * 0.25) + (project * 0.15)

    if Grade > 100:
        print("Grade is Over 100!")
    elif Grade >= 75:
        print("You PASSED!!")
    elif Grade < 75:
        print("Good Luck Next Life :( ")
    else:
        print("Huh?")