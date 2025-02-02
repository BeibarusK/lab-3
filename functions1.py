#Functions 1
 
#1 
def grams_to_ounces(grams): 
    ounces=28.3495231 * grams 
    print(ounces) 
grams=int(input("How many grams: ")) 
grams_to_ounces(grams) 
 
#2 
def fahrenheint_to_centigrade(F): 
    C = (5 / 9) * (F - 32) 
    print(C) 
F=int(input("Enter Fahrenheint: "))
fahrenheint_to_centigrade(F) 
 
#3 
def numbers(heads,legs):
    head1 = heads*2
    head2 = legs-head1
    rabbit = head2/2
    chicken = heads - rabbit
    return int(rabbit),int(chicken)

print(numbers(35,94))

 
#4 
def filter_prime(numbers): 
    for x in numbers: 
        if x==2 or x==3 or x==5 or x==7: 
            print(x) 
        elif x>10: 
            if x%2!=0 and x%3!=0  and x%5!=0 and x%7!=0: 
                print(x) 
numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14] 
filter_prime(numbers)
 
#5 
def permutations_of_string(str): 
    for i in range(len(str)):
        if len(str) == 1:
            return str
        
    permutations = []
    for i in range(len(str)):
        current = str[i]
        remaining = str[:i] + str[i+1:]

        perms = permutations_of_string(remaining)

        for j in range (len(perms)):
            permutations.append(current + perms[j])
    
    return permutations
        
    

str = "abc"
print(permutations_of_string(str))

#6 
def reverse_string(str):
    string=[]
    word=""
    for i in range(0,len(str)):
        if str[i]!=" ":
            word=word+str[i]
        else:
            string.append(word)
            word=""
    string.append(word)
    string.sort(reverse=True)
    return string
str1="We are ready" 
print(reverse_string(str1)) 
 
#7 
def has_33(nums):
    for x in range(len(nums)):
        if x>len(nums)-2:
            break
        elif nums[x]==nums[x+1]==3:
            return True
    return False

print(has_33([1, 3, 3]))#True
print(has_33([1, 3, 1, 3]))#False
print(has_33([3, 1, 3]))# False"""

#8 
def spy_game(nums): 
    a=0 
    for i in range(len(nums)): 
        if i>len(nums)-3: 
            break 
        elif nums[i]==0 and nums[i+1]==0 and nums[i+2]==7: 
            return True
    return False
print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,7,2,0,4,5,0])) #False
 
#9 
def volume_of_sphere(radius):
    volume=4/3*(3.14*pow(radius,3))
    return volume
print(volume_of_sphere(60))
#10 

def unique_elements(list):
    count=0
    list1=[]
    for x in list:
        for y in list:
            if x==y:
                count=count+1
        if count==1:
            list1.append(x)
        count=0        
    return list1
print(unique_elements([1,1,1,1,1,1,2]))
#11 
 
str="madam"
 
def is_palindrome(str): 
    str1=str[::-1] 
    if str==str1: 
        return True 
    else: 
        return False
print(is_palindrome(str)) 
 
#12 
def histogram(n): 
    for x in n: 
        for i in range(x): 
            print('*',end='') 
        print() 
n=[4,9,7] 
histogram(n) 
 
#13 
 
import random 
number=random.randint(1,20) 
x=0 
count=0 
name=input("Hello! What is your name?") 
print(f"Well,{name}, I am thinking of a number between 1 and 20.") 
while(x!=number): 
    count+=1 
    print("Take a guess") 
    x=int(input()) 
    if x>number: 
        print("Your guess is too high.") 
    elif x<number: 
        print("Your guess is too low.") 
    else: 
        print(f"Good job, {name}! You guessed my number in {count} guesses!")