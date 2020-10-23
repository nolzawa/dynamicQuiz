#Dynamic Quiz Creation and Game

#quiz creator
# key in the question and the options and answer
# store into a dictionary/list

#quiz participants
# answer with the valid a b c
# score

questionList = {} #empty dictionary
list = [] #temporary list to contain the options for the question

options = ['a', 'b', 'c']
score = 0
max_qn = 1

#quiz creator

num = input("How many question is this quiz?: ")
max_qn = int(num)

for i in range(max_qn):
    question = input("Please key your question: ")
    for x in range(3):
        if x == 0:
            option = input("Please enter an option for a): ")
            list.append(option)
        if x == 1:
            option = input("Please enter an option for b): ")
            list.append(option)
        if x == 2:
            option = input("Please enter an option for c): ")
            list.append(option)

            valid_answer = 0
            while valid_answer == 0:
                answer = input("What is the correct answer? a/b/c: ")
                if answer in options:
                    list.append(answer) #pos 3 will be compared for participant's answer
                    valid_answer = 1
                else:
                    answer = input("Please only enter a/b/c: ")
                    valid_answer = 0

        questionList[question] = list
    list = [] #clear

#print(questionList)

print("=========================================================\n")

print("QUIZ")

count = 1

for qn in questionList:
    print(f'Question {count}: {qn}')
    print(f' a) {questionList[qn][0]}')
    print(f' b) {questionList[qn][1]}')
    print(f' c) {questionList[qn][2]}')
    valid_input = 0 #check against options and user input

    u_answer = input("Please enter a/b/c: ").lower()
    while valid_input == 0:
        if u_answer in options:
            valid_input = 1
            if u_answer == questionList[qn][3]:
                print("You are correct!\n")
                score+=1
            else:
                print(f'Sorry, the correct answer was : {questionList[qn][3]}')
        else:
            u_answer = input("Please enter only a/b/c: ")
            valid_input = 0
    count+=1

print(f'You have scored {score}/{max_qn} correctly!')


