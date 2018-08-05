class Person:
    def __init__(self,name,age,address):
      self.n = name
      self.a = age
      self.add = address
    

    def get_value(self):                    #  def getValue 
       print("My name is "+self.n)
       print("My age is  "+str(self.a))
       print("My Address is  "+self.add)






ab = Person("Abhishek",24,"bhagriya mohalla Narayangarh")

ab.get_value();
