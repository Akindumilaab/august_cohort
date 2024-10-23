# students = ['ola', 'ope', 'bola']
# scores = [10, 20, 30]
# print(type(scores))
# # print(min(scores))
# # print(students.index('ola'))
# # index_num = min(students.index(scores))
# # print(index_num)
# final_score = 0
# num_students = int(input(" Input the number of student  registered for the test: "))
# students = []
# for each in range(num_students):
#     user = input(f'Input the student {each+1} name: ')
#     students.append(user)


# ques_and_ans = {
#     "1. what is the capital of Ghana a.) accra b.) Abuja" : 'a', 
#     "2. what is the capital of Nigeria a.) accra b.) Abuja": 'b',
#     "3. What is the capital of osun state a.) Oshogbo b.lagos c. osun": 'a',
#     "4. What is the colour of Nigeria flag? a.) White b.) Green c.) Green and white": 'c'

# }
# for stud in students:
#     score = 0
#     print(f'{stud} take your test:')

#     for question, answer in ques_and_ans.items():
#         print(question)
#         user = input('Enter your answer => ')
#         if user == answer:
#          print('Correct')
#          score+=5 
#         else: 
#           print('wrong')
    
#     print(f'{stud} Your finalscore is {score}/20')
#     print('-----------')
    
# print(sum(score))


# ticket = 10
# while ticket > 0:
#     print(f' Tickect is remaing {ticket}')
#     age = int(input('Enter your age: '))
#     if age <18:
#         print('Youre not eligible')
#         continue
    
#     else:
#         ticket -= 1
# else:
#     print('Ticket is exhauted')


# user = []
# while True:
#     name = input('Input your name: ')
#     option = input('press 1 to stop or enter to continue: ')
#     if option == '1':
#         break
#     else:
        # user.append(name)

#                 # for loop 
# num_student = int(input('Enter the number of student registered for this test: '))
# students = []
# for each in range(num_student):
#     user = input(f'input student {each + 1} name: ')
#     students.append(user)
# for stud in students:
#     print(f'{stud} take your test')








                # to do list
all_todo = []

def dashbord():
    print('''
        Welcome to myTodo App
        1. Create a todo
        2. Edit a todo
        3. Delete todo
        4. view todo
        #. exit

''')
    option = input('options: ')
    if option == '1':
        createTodo()
    elif option == '2':
        editTodo()
    elif option == '3':
        deleteTodo()
    elif option == '4':
        viewTodos()
    elif option == '5':
        print("Exiting the app.")
        return
    else:
        print('Invalid option')

def createTodo():
    todo = input('Enter your todo: ')
    all_todo.append(todo)
    print(f'Todo {todo} successfully created')
def  editTodo():
     viewTodos()
     index = int(input('Enter the number of  the todo you want to edit: ')) -1
     if 0  <= index < len(all_todo):
         new_todo = input('Enter the new todo: ')
         all_todo[index] = new_todo
         print(f'Todo {index + 1} successfully edited')
     else:
         print('Invalid index')
def viewTodos():
     



         








