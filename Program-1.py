class cal:                          # creating a class
    def __init__(self,a,b):
        self.a=a 
        self.b=b 
    def add(self):
        return self.a+self.b 
    def sub(self):
        return self.a-self.b 
    def mul(self):
        return self.a*self.b 
    def division(self):
        return self.a/self.b 

a=float(input())  # input a
b=float(input())  # input b
operation=input() # input type of operation (addition,subtraction,multiplication,division)
obj=cal(a,b)
if operation =="addition":
    print(obj.add())
if operation=="subtraction":
    print(obj.sub())
if operation =="multiplication":
    print(obj.mul())
if operation=="division":
    print(obj.division())