# OOp -> Object oriented programing
class PhoneTemplate:
    # state the properties and function
    def __init__(self):
        self.model = 'Iphone xr'
        self.color = 'Black'
        self.state = True
    def home(self):
        if self.state:
            user = input('''
            1. make a call
            2. switch on/off
        ''')
            if user == '1':
             self.make_a_call()
            elif user == '2':
             self.switch_off_or_on()
            else:
             print('Error')
             self.home()
        else:
           user = input('The phone is off. press 1 to switch on: ')
           while user != 1:
              user = input('The phone is off. Press 1 to switch on: ')
           else:
            self.switch_off_or_on()

    def make_a_call(self):
        print(f'The {self.model} can make calls')

    def switch_off_or_on(self):
        if self.state:
            print('swithing off...')
            self.state = False
        else:
            print('swithing on....')
            self.state = True
    
# phone1 = PhoneTemplate()
# phone2 = PhoneTemplate()

# phone1.model = 'Iphone15'
# print(phone1.model)
# print(phone2.model)



class Calculator:
   def __init__(self):
      self.name = 'Casio'
    
   def calculate(self):
      self.value1 = float( input('Value1: '))
      self.value2 = float(input('Value2: '))
      options = input(""" 
                1. Addition
                2. Subtraction
                3. Multiply
                4. Exit

    """)
   
      if options == '1':
         self.addition()
      elif options == '2':
         self.Subtraction()
      elif options == '3':
         self.Multiplication()
      else:
         pass
      
   def addition(self):
      print(f"Answer = {self.value1 + self.value2}")
      user = input('press 1 to exit and enter  to continue')
      if user == '1':
         exit()
      else:
         self.calculate()


   def Subtraction(self):
       print(f"Answer = {self.value1 - self.value2}")
       user = input('press 1 to exit and enter  to continue')
       if user == '1':
         exit()
       else:
        self.calculate()

   def Multiplication(self):
       print(f"Answer = {self.value1 + self.value2}")
       user = input('press 1 to exit and enter  to continue')
       if user == '1':
         exit() 
       else:
         self.calculate()

      
      
# mycalc = Calculator()
# mycalc.calculate()



class Ussd:
   def __init__(self):
     self.network = 'bimsnetwork'


   def dashbord(self):
     
         user = input('input Ussd code: ')
         if user == '*312#':
            print('Welcome to BimsNetwork service')
            ussd = input('''
            1. data plan
            2. Airtime recharge
            3. share data
            4.Borrow data/Airtime
            0. Exit
                   
          choice: ''')
            
            if ussd == '1':
               self.Dataplan()
            elif ussd == '2':
              self.Airtime() 
            elif ussd == '3':
               self.share_data()
            elif ussd == '4':
               self.Borrow_data_airtime()
            elif ussd == '0':
               exit()
            else:
               print('invalid code.')
               self.dashbord()
         else:
            print('Invalid code. Try again')
            print('Daial *312# to iniate a transaction')
            self.dashbord()

   def Dataplan(self):
      choose_plan= input('''
      1. Weekly plan
      2. Daily plan
      
      choice: ''')
      if choose_plan == '1':
         print('Weekly plan activated. Thank you for using this service')
         self.dashbord()
         

      elif choose_plan =='2':
         print('daily plan activated. Thank you for using this service')
         self.dashbord()
         

      else:
         print('Choice plan not valid')
         self.dashbord()

   def Airtime(self):
      amount = int(input('Amount: '))
      if amount > 5000:
         print("You're not eligible for this amount")
         self.dashbord()
      else:
         print('Recharge successful!')
         self.dashbord()

   def share_data(self):
      num = int(input('Input others number: '))
      if len(num)!= 11:
         print('Pls check the number again')
         self.dashbord
      else:
         print('successfuly')
         self.dashbord()
   
   def Borrow_data_airtime(self):
      Borrow = input('''
        1.Borrow Airtime
        2.Borrow Data
                     
        choice: ''')
      if Borrow == '1':
         self.Borrow_Airtime()
      elif Borrow =='2':
         self.Borrow_data()
      else:
         print('Check code again')
         self.dashbord()

   def Borrow_Airtime(self):
      amount= int(input('Input amount: '))
      if amount > 500:
         print("You're not eligible")
         self.dashbord()
      else:
         print(f'Airtime succefully recharged.\n your balance is {amount}')
         self.dashbord()

   def Borrow_data(self):
      amount= int(input('Input amount: '))
      if amount > 700:
         print("You're not eligible")
         self.dashbord()
      else:
         print(f'You have recived{ amount} mb.\n Continue browsing till kingdom come.')
         self.dashbord()

# app = Ussd()
# app.dashbord()

class calc:
   def __init__(self):
      self.model = 'propo'
   
   def home(self):
      self.value1 = int(input('input val1: '))
      self.value2 = int(input('input val2: '))
      options= input('''
      1. Addition
      2. subtraction
      3. exit
 choice: ''')
      if options == '1':
         self.Addition()
      elif options == '2':
         self.Subtraction()
      elif options == '3':
         exit()
      else:
         print('Invalid choice')
         self.home()
   def Addition(self):
      print(f'Answer = {self.value1 + self.value2}')
      user = input('press 1 to exit or enter to continue: ')
      if user == '1':
         exit()
      else:
         self.home()

   def Subtraction(self):
      print(f'Answer = {self.value1 - self.value2}')
      user = input('press 1 to exit or enter to continue: ')
      if user == '1':
         exit()
      else:
         self.home()

# cal = calc()
# cal.home()

#                                     parametized class
class Human:
   def __init__(self, name):
      self.name = name
   def introduce(self):
      print(f'My name is {self.name}')
name = input('Name: ')
# ayo = Human()
# ayo.introduce()

class Human():
   def __init__(self):
      self.name = input('name: ')
   def introduce(self):
      print(f'My name is {self.name}')
# ayo= Human()
# ayo.introduce()

                                             # Inheritance
class Parent:
   def __init__(self):
      self.surname = 'Tinubu'
      self.firstname = 'Ahmed'
      self.hobby = 'Playing golf'
      
   def introduce(self):
      print(f'My name is {self.firstname} {self.surname}. I love {self.hobby}')
father = Parent()
father.introduce()


      


      



      

      
         


      

      
      