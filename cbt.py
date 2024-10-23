# cbt test
import time as tm
# score = 0
# Qustion1 = input('What is your mothers name?\n a. Titi\n b. Ronke\nans:  ')
# Qustion2 = input('What year did Nigeria gain independent. \n a. 1920 \n b. 1940\n c.1960\nans: ')
# Qustion3 = input(' What is the colour of Nigeria flag?\n a. White\n b. Green\n c. Green nd white\nans: ')
# if Qustion1 == 'a'.lower():
#     score += 2
#     print(f'youre correct, your score is {score}/6')
# else:
#     print(f'Incorrrect')

# if Qustion2 == 'c'.lower():
#     score += 2
#     print(f"You're correct , your score is {score}/6")
# else:
#     print(f'Incorrect')
# if Qustion3 == 'c'.lower():
#     score += 2
#     print(f"You're correct, your score is {score}/6")
# else:
#     print(f'Incorrect')
# print(f"your final score is {score}/6")
# if score == 6:
#     print(f'what an excellent result')
#     tm.sleep(2)
#     print('Congratulation, keep it up')
# else:
#     print(f'You tried but you can do better!')



 
    
num_students =int(input(f'Input the number of registered student: '))
students = []
for each in range(num_students):
    user =input(f'Enter student {each + 1} name: ')
    students.append(user)
print(students)
score = 0
for stud in students:
    print(f"{stud} take your test")
    question1 = '1. What is the capital of osun state\na.) Oshogbo b.) Ife c.)Ilesha'
    print(question1)
    ans = input('Answer: ').strip().lower()
    if ans == 'a':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question2 = "2. What year did Nigeria gain independent. \n a. 1920 \n b. 1940\n c.1960 "
    print(question2)
    ans = input('Answer: ').strip().lower()
    if ans == 'c':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question3 = "3. What is the colour of Nigeria flag?\n a. White\n b. Green\n c. Green nd white "
    print(question3)
    ans = input('Answer: ').strip().lower()
    if ans == 'c':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    question4 = "4. Who designed the Nigeria flag\n a. Titi Olayemi\n b. Taiwo Akinkunmi\n c. You\nans: "
    print(question4)
    ans = input('Answer: ').strip().lower()
    if ans == 'b':
        print('Correct')
        score += 5
    else:
        print('Incorrect')
    print(f"your final score is {score}/20")
    print(score)
    if score == 20:
     print(f'what an excellent result')
     tm.sleep(2)
     print('Congratulation, keep it up')
    else:
     print(f'You tried but you can do better!')

    

    





# num_students = int(input(f"Enter the nuber of student that are registerd for cbt test: "))
# students = []
# for each in range(num_students):
#     user =input(f"Enter student {each+ 1}name: ")
#     students.append(user)
# print(students)
# for stud in students:
#     print(f"{stud} take your test")