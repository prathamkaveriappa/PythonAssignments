
class Car():
    def __init__(self,make,model,color,price):
        self.make = make
        self.model = model
        self.color = color
        self.price = price
    def start(self):
        self.speed=0
    def move(self):
        self.speed=self.speed+5
    def stop(self):
        self.speed=0
    def info(self):
        print('\nMake of the car is: ',self.make,'\nModel of the car is: ',self.model,'\nColor of the car is: ',self.color,'\nSpeed of the car is: ',self.speed, '\nPrice of the car is: ',self.price)
obj=Car('Volkswagen','Passat','Black',2200000)
obj.start()
obj.info()
obj.move()
obj.move()
obj.move()
obj.info()
obj.stop()
obj.info()      
