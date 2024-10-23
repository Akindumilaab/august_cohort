                                                # Ussd app
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
      if num > 9 and num < 9:
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

app = Ussd()
app.dashbord()



                        #    Alata Calculator
class calc:
   def __init__(self):
      self.model = 'Casio'
   
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

cal = calc()
cal.home()



      

      
         


      

      
      