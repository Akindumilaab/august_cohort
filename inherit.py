                              # Inheritance
class Parent:
   def __init__(self):
      self.surname = 'Tinubu'
      self.firstname = 'Ahmed'
      self.hobby = 'Playing golf'
      
   def introduce(self):
      print(f'My name is {self.firstname} {self.surname}. I love {self.hobby}')
    #   return(f'My name is {self.firstname} {self.surname}. I love {self.hobby}')# this is another method
# father = Parent()
# father.introduce()

class Child(Parent):
   def __init__(self):
      super().__init__()
      self.firstname = 'seyi'
      self.occupation = 'Politician'

   def introduce(self):
       print(f'Hello everyone, My name is {self.firstname} {self.surname}, I am a {self.occupation}')
       return super().introduce()

    # info = super().introduce()
    # print(f'{info}. I am also  {self.occupation}')

   def run(self):
      print(f'{self.firstname} can run fast and he  is also a {self.occupation}')
# child1 = Child()
# child1.introduce()
# child1.run()

class Grandchild(Child):
   def __init__(self):
      super().__init__()
      self.firstname = 'Tola' 
      self.surname = 'Ahmed'
      self.height = 'undefined'
      self.complextion = 'light'
   
   def intro(self):
        print(f'My name is {self.firstname} {self.surname}. I love {self.hobby}. My height is {self.height} and my complexion is {self.complextion}' )
# g_child1 = Grandchild()
# g_child1.intro()

class User:
   def __init__(self):
      pass
    
 
   





      