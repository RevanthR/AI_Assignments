'''
Question::
    
You decide you want to play a game where you are hiding a number from someone.
Store this number in a variable called 'answer'. Another user provides a number called 'guess'. 
By comparing guess to answer, you inform the user if their guess is too high or too low.

'''
#Solution::
answer=int(input("you  enter a number:"  ))
guess=int(input("Ask other person to enter a number:"))

if(answer > guess):
    print("number that is guessed is smaller")
elif(answer < guess):
    print("Number that is guessed by other is more than your number")
else:
    print("Both are Same")
    
    
'''   
Question::
Write a for loop below that will print out every whole number that is a multiple of 5 
and less than or equal to 30.

'''
#Solution::
for i in range(30):
    if(i%5 == 0):
        print("number:",i)
'''
output::        number: 0
                 number: 5
                 number: 10
                 number: 15
                 number: 20
                 number: 25
'''

'''
Question::
Write a while loop that finds the largest square number less than an integerlimit and 
stores it in a variable nearest_square.
 A square number is the product of an integer multiplied by itself,
 for example 36 is a square number because it equals 6*6.

'''  
#Solution::
limit = 100
num = 0 
while (num +1)**2 < limit:
    num += 1
nearest_square = (num)**2


print(nearest_square)
                 