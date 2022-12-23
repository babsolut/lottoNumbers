#lottery numbers
import random
#initialise an empty list that will be used to store the 6 lucky numbers!
lotteryNumbers = []

for i in range(0,6):
    number = random.randint(1,50)
    #check if this number already been picked and...
    while number in lotteryNumbers:
        #...if it has, pick a new number instead
        number = random.randint(1,50)
    #Now that we have a unique number, let's append it to our list.
    lotteryNumbers.append(number)
    
    #sort the list in ascending order
lotteryNumbers.sort()
    
userNumbers = []
for i in range(0,6):
    number = int(input("Please enter a number between 1 and 50: "))
    while(number in userNumbers or number<1 or number>50):
        print("Invalid number, please try again.")
        number = int(input("Please enter a number between 1 and 50: "))
        
    userNumbers.append(number)
    
#Display the list on screen:
print(">>> Today's lottery numbers are: ")    
print(lotteryNumbers)

print(">>>Your selections: ")
print(userNumbers)

counter = 0
for number in userNumbers:
    if number in lotteryNumbers:
        counter +=1
print("You guessed  " + str(counter) + " number(s) correctly!")