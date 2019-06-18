class student():
    def register(self,regno,name,standard, sec):
        self.regno=regno
        self.name=name
        self.standard=standard
        self.sec=sec
    def information(self):
        print('\nRegister Number: ',self.regno,'\nName: ',self.name,'\nStandard: ',self.standard,'\nSection: ',self.sec)
bhavikaa=student()
bhavikaa.register(101,'Bhavikaa','9','A')
bhavikaa.information()

shlokaa=student()
shlokaa.register(102,'Shlokaa','9','B')
shlokaa.information()

class calculator:
    
    def addition(x,y):
        added = x + y
        print(added)
        
    def subtraction(x,y):
        sub = x - y
        print(sub)

    def multiplication(x,y):
        mult = x * y
        print(mult)

    def division(x,y):
        div = x / y
        print(div)