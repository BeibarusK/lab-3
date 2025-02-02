#1
class String:
    def __init__(self):
        pass
    
    def getString(self):
        self.string = input()
        pass
    
    def printString(self):
        return (self.string).upper()

string=String()
print(string.getString())
print(string.printString())

#2
class Shape:
    class Square:
        def __init__(self,length):
            self.length=length
            self.area=0
        def area_of_shape(self):
            self.area=self.length*self.length
            return self.area
    def area_of_shape(self):
        self.area=0
        return self.area
a=Shape.Square(41)
b=Shape()
print(a.area_of_shape())
print(b.area_of_shape())

#3
class Rectangle(Shape):
    def __init__(self,width,length):
        self.width=width
        self.length=length
    def compute_area(self):
        area=self.length*self.width
        return area
a=Rectangle(20,30)
print(a.compute_area())

#4
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def show(self):
        return self.x,self.y
    
    def move(self,x,y):
        self.x=x
        self.y=y
    def dist(self):
        return self.y-self.x
a=Point(1,4)
print(a.show())
print(a.move(4,7))
print(a.show())
print(a.dist())

#5
class Account:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,x):
        self.balance=self.balance+x
        return self.balance
    def withdrawal(self,x):
        if x>self.balance:
            return "Withdrawals may not exceed the available balance"
        else:
            self.balance=self.balance-x
            return self.balance
a=Account("Beibarys",140000)
print(a.withdrawal(12000))
print(a.deposit(11000))
print(a.withdrawal(500000))

#6
class Prime_Filter:
    def __init__(self,nums):
        self.nums=nums
    def filter(self):
        prime_numbers=[]
        for x in self.nums:
            if x<10:
                is_prime=lambda x:True if x==2 or x==3 or x==5 or x==7 else False
                if is_prime(x)==True:
                    prime_numbers.append(x)
            else:
                is_prime=lambda x:True if x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0 else False
                if is_prime(x)==True:
                    prime_numbers.append(x)
        return prime_numbers

a=Prime_Filter([1,2,4,5,7,85,1,45,2,5,75,1,11])
print(a.filter())