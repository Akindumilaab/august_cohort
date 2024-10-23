# python output command
# print(2+2) 
# Type of commenting
# 1 single line commenting : #
# 2 multiple-line comment : """ """ or ''' '''


# python variable
# 1 variable name
# 2. assignment operators
# 3.value
Student = 'Daniel'
# print(Student)

# casing
# snake casing
the_first_student = 'dd'
# pascal casing
TheFirstStudent = 'dd'
# camel casing
theStudent = 'dd'
age = 20
# print('Age: '+ str(age))

age = age + 1
# print('Age: '+ str(age))

name = 'Abimbola Akindumila'
age = '21'
complexion = ' Dark'
satus = 'single'

# print('My name is ' + name  + " i am " + age + 'years old',  ' i am ' + complexion + " in complextion and also single")
# N = 20
# print(f"+{N}")

# python Data types
# 1.) Number types:
# i. integers e.g 10, 30, 343, they are whole number 
# ii.float e.g 0.2, 10.3, 34.55, they are decimal numbers
# iii. complex e.g 3+4J

# object is anything that has a property, it is an obj because it can perform a functions
# num = 30
# print(type(num))

# converting to an int or String
# num = 3.0
# print(int(num))
# print(str(num))

# 2.) text type
# i. string str() e.g 'Abimbola'

# 3.) Boolean Type  bool() e.g True or False
# isMarried = True
# isMarried = False
# print (isMarried)
# converting bool() to an int
# print(int(isMarried))
# print(float(isMarried))
# print(str(isMarried))

# 4.) sequence type 
# i. tuple tuple() e.g ('ope', 'mercy', 'True', 34)# singleline multiple variables
# ii. list list () e.g ['ope', 'mercy', 'True', 34]
# iii. Range range() e.g range(20)
myTuple = ('ope', 'mercy', 'True', 34)
# print(myTuple)
# print(type(myTuple))
# print(len(myTuple))
# print(list(myTuple)) converting tuple  to a list
# myTuple.
# myList = ['ope', 'mercy', 'True', 34]
# myList.
# print(myList)
# print(type(myList))
# print(len(myList))
# print(tuple(myList)) # converting  list to a tuple

# var = range(20)
# print(list(var))
# var = range(1,21)
# var = range(1,1000,2)
# var = range(1,21, 2) the 2 would  take 2 steps ahead 
# print(list(var))

# 5. Mapping type 
# i. dictionary dict() e.g {'name':'Bim', 'Age':20}  # key:value
person1 = {
    'name': 'Bim',
    'age' : 20,
    'isMarried': True
}
# print(person1)
# print(type(person1))
# print(person1['name'])  give me person one at the key of name
# print(person1['isMarried'])

# 6. set types set is unordered
# set set() e.g {'ope', 'mercy' , 'aliya', 'daniel'}
# myset = {'ope', 'mercy' , 'aliya', 'daniel'}
# num = {9,3,4,3,5,3,5,6,8,5,2,}   note that set will not scarter it for numbers and is won't duplicate the numbers 
# print(myset)
# print(type(myset))
# print(num)

# 7. Binary types #binary numbers
# i. byte
# bytes()
# ii byte array

# print(bin(10))

        # python operators
# 1. Arithmetic = +,-,*,/,%,//,**
# print(5//2)
# print(5%2)
# 2. assignment operator =,+=(increment), -=(decrement),*=,/=,//=,**=
num = 5
# num += 5
# print(num)
# 3. comparison operator = ==, !=, <,>,>=,<=

# conditional statement
# if num == 5:
    # print('num is 5') 
# else:
    # print('num is not equals to 5')

# name = input('input your username: ')
# password = input('input your password: ')
# comfirmPassword = input('confirm password')

# print(name,password)
# if(len(password) < 8):
    # print('password is inavlid')
    
# else:
    # print('password is valid')  

        # nested if\else stateent
    # if(password == comfirmPassword):
            # print('password match.continue')
    # else:
            # print('password is incorrect')

# 4. Logical operators = and, or, not
#  AND
# A     B       Result
# 1      1        1
# 0      1        0
# 1      0        0
# 0      0        0

        # OR
# A     B       Result
# 1      1        1
# 0      1        1
# 1      0        1
# 0      0        0

    #   NOT
# A      Not A
# 1       0
# 0       1

# username = 'Abimbola'
# password = '12345'
# print('login')
# inp_user = input('username: ')
# inp_pass =input('password: ')
# if(inp_user == username and inp_pass == password):
#       print('login successful')
# else:
#       print('wrong username or password')

isActive = True

# if(not isActive):
#     print('Access denied.. login')
# else:
#     print('Access granted')

# isMarried = False 
# if(isMarried):
#     print('you do well bro')
# else:
#     print('you no try aswear')

# isMarried = True
# if not isMarried:
#      print('you no try aswear')
# else:

#     print('you do well bro')

# 5. membership operator = in not in
favourite_dishes = ['yam', 'rice' , 'beans']
# print('rice' not in favourite_dishes)
# print('Rice' not in favourite_dishes)

# 6. identity operator = is, is not
# num = 4
# num2 = 4
# print(num is not num2)
# print(num is num2)

# value1 =int(input('input  val1:')) 
# value2 = int(input('input  val2:'))
# options = input('''
#             1. Adition
#            2. subtraction
#            3. multiplication
#            4. division
#            5. exit
#        choice: ''')
# if options == '1':
#     print(value1 + value2)
# elif options == '2':
#     print(value1 - value2)
# elif options == '3':
#     print(value1 * value2)
# elif options == '4':
#     print(value1 / value2)
# elif options == '5':
#     print('Thank you for the arithemetics.')
#     exit()
# else:
#     print('you entered an invalid number. Kindly check the number you entered.')


# python strings
# strings are sequence of charaters. They can be enclosed in single quotes or double qoutes
student_name = 'Daniel' #[D,a,n,i,e,l]
# print(len(student_name))
# print(student_name[0])
# print(student_name[-1])
# slicing
# print(student_name[:])
# print(student_name[1:3]) # start from 1 and at 3
# print(student_name[1:]) #start from 1 end at nothing
# print(student_name[:3]) # end at 3
# num = []  # list
# num = ()# tuple
# num = {}# set
# num = {value: key} # dictionary
# print(student_name.lower())
# print(student_name.upper())

expression = 'Daniel is a python programmer at Sqi college of ICT  '
# print(expression.capitalize())
# print(expression.title())
# print(len(expression))
# print(len(expression.strip('-//'))) #this is to strip away any of this charters if they are in the expression
# print (len(expression.strip())) this is to strip the space in the sentence
# print (expression.count('a')) # this is to count all the 'a' in the expression
# print(expression.count(' a '))# this is to count the 'a standing alone
# print(expression.count('Daniel'))
# print(expression.split('a')) this is going to spilt out  all the a in the expression
# print(expression.strip())
# print(expression.strip('/'))
# item = ['+234', '9042823291']
# print(''.join(item))
# print(expression.startswith('Daniel'))
# print(expression.replace('Daniel', 'Aliyah'))
#                                Escape charaters 
# \ backslash n \n
                        # python collections/array
# list, tuple, set, dictionary
# list =  Are ordered, mutable or changeable, can be indexed ,accept  duplicate value y
# students = ['daniel','Aliyah', 'mercy', 'ope', 'mercy']
# print(students[-4:-1])
# print(students[::-1])  #this would be reversed
# print(students[4])
# # print(students[])
# students[:2] = ['Abimbola', 'Abimbola']

# students[0], students[1] = 'Abimbola', 'Abimbola'
# print(students)
# students.reverse()
# students.append('Abimbola')
# students.extend(['Abimbola','John','Shola'])
# print(students)

# arr = [
#     ['Banana','Apple', 'orange'[23,45]],
#     ['Rice', 'Beans'],
#     'water', 324, True
# ]
# print(arr)
# print(arr[0][0])
# print(arr[0][3][1])

# students.remove('ope')
# students.pop(1)
# students.clear()
# students.insert(0, 'Abimbola')
# print(students)

#    for looop
# for each_student in students:
#     print('Welcome,', each_student)
#     print('----------------------')

# for x in range(20):
#     print(x)

# info = []

# for x in range(5):
#     name = input(f'name{x + 1}: ')
#     info.append(name)
# # print(info)

# for each in info:
#     print(each, 'is a member.')
students = ['Ayo', 'Dele', 'Ade']
scores = [21, 23, 44]
sum_scores = sum(scores)
lenght = len(scores)
avg_score = sum_scores/lenght
# print(f"Average score is {avg_score}")
# print(min(scores))
# print(max(scores))

# for student, score in zip(students,scores):
#     print(f'{student} scored {score}')

questions = [
    
    "1. what is the capital of nigeria a.) accra b.) Abuja"
    "2. what is the capital of Nigeria a.) accra b.) Abuja"
]
answers = [
    'a'
    'b'
]

# for quest, ans in zip(questions, answers): 
#     print(quest)
#     answer = input('Answer: ')
#     if answer.lower() == ans:
#         print('correct')
#     else:
#         print('wrong')


                                    # Tuples
#  immuntable or unchangleable, it can be indexed, allows duplicate values, ordered
# tuple() or (), tuple are used to collect information that has to be secured and it cant be changed ie. information like password, emails

# fruits = ('Banana', 'orange', 'Apple', 'orange')
# print(fruits)
# print(len(fruits))
# print(fruits[2])
# print(fruits[0:3])
# fruits[0] = 'watermelon'# tuple is not changable, so it wont change, and to change it now you need to convert
# new = list(fruits)
# new[0] = 'watermelon'
# fruits = tuple(new)
# print(fruits)# it has changed to waterelon by converting

# var = ('favor') # this is an oridinary string
# var2 = 'favor', # with this without bracket, so far it has a comma its a tuple
# print(type(var2))

# tuple can only perform 2 functions which are count and index
# print(fruits.count('orange'))
# print(fruits.index('apple'))

                #  list of tuple
# ques_and_ans = [
#     ("1. what is the capital of nigeria a.) accra b.) Abuja", 'b')
#     ( "2. what is the capital of Nigeria a.) accra b.) Abuja", 'a')
# ]

# for quest, ans in ques_and_ans:
#     print(quest)
#     print(ans)


                    #   set
# set is immutable or unchanabale, it can be indexed, its not ordered, it doesnt accept duplicate value, its the direct opposit of list
# set() or {}
fruits = {'Banana', 'Mango', 'Apple', 'Mango', 'orange'}
# print(fruits.)
# print(len(fruits))
# fruits.add('tomato') # this can only work for one item
# print(fruits)
# fruits.update(['tomato', 'grape'])
# print(fruits)
# fruits.remove('banana') # this wont work cos banana is not found as a lower case
# print(fruits)
# fruits.discard('Banana')
# fruits.clear()
# print(fruits)
# empty set # set()
# empty dict # {}

setA = {1, 3, 6, 7, 3, 4, 2, 5, 9, 0, 8}
setB = {12, 13, 2, 1, 11}
setC = { 3, 4}
# print(setA.union(setB))
# print(setA.intersection(setB))
# print(setA - setB)
# print(setA.difference(setB))
# print(setA.symmetric_difference(setB))
setA.intersection_update(setB)
# print(setA)
setA.symmetric_difference_update(setB)
# print(setA)
# print(setA.issuperset(setB))
# print(setA.issuperset(setC))
# print(setC.issubset(setA))
# print(setC.isdisjoint(setB))


                    # Dictionary wiill be at the key of and not indexed of
# ordered, it is changable, it doesnt not allow duplicate
# dict(key = value) or {key:value}
phone = {
    'model': 'iphone16',
    'color': 'Black',
    'rom'  :'128gb',
    'version':'ios 18',
    'owner':{
        'name': 'Abimbola',
        'address': 'Lagos'
    }
}
# print(phone['model'])
# print(phone['owner']['name'])
# phone['model'] = 'iphone18' # this is updating
# phone['models'] = 'iphone18' # this is adding a new model
# print(phone)
# print(phone.keys())
# print(list(phone.keys())[0]) # to get the index it will be convrted to a list
# for key in phone.keys():
    # print(key)
# print(phone.values())
# print(phone.get('models')) # this will throw none , which is better cos your code isnt meant to teerminate
# print(phone['models']) # this would terminate immdediately cos e have model and not models
# phone.update({'sold: True'})
# phone.pop('owner')
# print(phone)

# for val in phone.values():
    # print(val)
# print(phone.items())
# for key,value in phone.items():
    # print(key, value)
    # print(f'{key} => {value}')

# ques_and_ans = {
#     "1. what is the capital of nigeria a.) accra b.) Abuja" : 'b', 
#     "2. what is the capital of Nigeria a.) accra b.) Abuja": 'a'

# }
# for ques, ans in ques_and_ans.items():
#     print(ques)
#     user = input('answer: ').strip()
#     if user.lower() == ans:
#         print('correct')
#     else:
#         print('wrong')

        # todo application with a dictionary
# x = 10
# while x>1:
#     print('yo!')
#     x -= 1 

# students = []
# user = input('insert student name, press 1 to stop or enter to continue: ')
# while user != '1':
#     user = input('Input Name or 1 to stop: ')
#     students.append(user)
# print(students)


# user_db = []
# user = int(input('No of users: '))
# for x in range(user):
#     name = input(f'Name {x + 1}: ')
#     age = int(input("Age: "))

#     user-info = {}
#     user_db.append(name)


# user_db = {}
# user = int(input('No of users: '))
# for x in range(user):
#     name = input(f'Name {x + 1}: ')
#     age = int(input("Age: "))
#     user_db.update({x+1: (name, age)})

# print(user_db)


# user_db = []
# user = int(input('No of users: '))
# for x in range(user):
#     firstName = input(f'firstName {x + 1}: ')
#     lastName = (input(f"lastName: "))
#     email = (input(f'email: '))
#     password = int(input('Password: '))
#     user_db.append({x+1: {firstName, lastName, email, password }})
# print(user_db)

# user_db = []
# user = int(input('No of users: '))
# for x in range(user):
#     user = {
#         'firstName': input('firstname: '),
#         'lastname': input('secondname: '),
#         'email': input('email: '),
#         'password': input('password: ')
#     }
#     user_db.append(user)
# print(user_db)
 
# x = 10
# while x > 1:
#     print('yo', x)
#     x -= 1
 
# x = 0
# while x < 1:
#     print('yo', x)
#     x += 1


# users = []
# slot = 5
# while slot > 0:    
#     user = input('name: ')
#     users.append(user)
#     slot -= 1
# else:
#     print(' slot is exhausted')

# ticket = 10
# while ticket > 0:
#     print(f'ticket is remaining {ticket}')
#     age = int(input('Input your age: '))
#     if age < 18:
#         print('You are not welcome to the party')
#         break
#     else:
#          ticket -= 1
# else:
#     print('ticket is exhauted')

# user = []
# while True:
#     name = input('Enter your name: ')
#     option = input('Press 1 to stop or enter to continue: ')
#     if option == '1':
#         break
#     else:
#         user.append(name)



# def addition(value3, value2=20, value1=20):
    # print(f'answer = { value1 + value2}')

# addition(value1=23, value2=33, value3= 20)
# addition(10,20,30)
# addition()

# def call_my_name(name):
#     print(f'My name is {name} ')
# call_my_name('Bims')

# def family_name(Akinyele):
#     name = input('input your name:')
#     print(f'{Akinyele}')

def get_percent(score, total_score = 100):
    grade = (score/total_score) *100
    return grade
def check_grade():
    score = float(input('Score: '))
    total_score = int(input('Total score'))
    score_in_percent = get_percent(score, total_score)
    print(f'{score_in_percent}%')
    if score_in_percent > 70:
        print(f'Grade: A\nScore:{score_in_percent}%')
    elif score_in_percent > 64 and score_in_percent < 70:
        print(f'Grade: B\nScore:{score_in_percent}%')
    elif score_in_percent >50 and score_in_percent < 59:
        print(f'Grade: C')
    elif score_in_percent >= 40:
        print('Grade: D')
    else:
        print('grade: f. You Failed')
check_grade()

# print(get_percent(24.5, 30))

#                  Types od variables
# global and loacal variable
# val1 = 10  # global vriable
# val2 = 10
# def add(): 
#     global val2
#     val2 = 20
#     print(val1 + val2)

# def sub():
#     add()
#     print(val2)
    
# add()
# sub()
