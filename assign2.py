# -*- coding: utf-8 -*-
"""assign2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zTg1IH3te-7RhjklnEsnC3hJuH5PhaeJ
"""

#Question1

answer = [65]
guess = [17,16,10]

if guess>answer:
    print("guess is too high")
else:
    print("guess is too low")

#Question2:

for num in range (1,30):
    if num%5==0:
        print(num)

#Question3:  


limit = 100
num = 0 
while (num +1)**2 < limit:
    num += 1
nearest_square = (num)**2
print(nearest_square)