account_balance = 100
def dashbord():
     print('''
    Welcome to my Bank
        1. withdraw
        2. Deposite
        3. Check Balance
        4.  Exit

    ''')
     options = input('options: ')
     if options == '1':
          withdraw()
     elif options == '2':
          Deposite()
     elif options == '3':
          Check_Balance()
     elif options == '4':
          Exit()
     else:
          print('Invalid code. Try again')
          dashbord()

def withdraw():
     global account_balance
     amount = float(input('Amount: '))
     if amount > account_balance:
          print('Insufficient balance')
     else:
          account_balance -= amount
          print(f'You withdraw  #{amount} and your balance is #{account_balance}')

     
withdraw()