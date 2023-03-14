#########################################
# CS 1110A - Programming in Python      #
# Module 2 - Exercise 4 - Using Loops   #
# Author: Lamech Israel                 #
# Date:   01/17/2023                    #
#########################################


# Input

data1 = [12, 10, 32, 3, 66, 17, 42, 99, 20]
data2 = [14, 7, -12, 88, -17, 22, -5, 18]


# Processing

def calculate(data):
    initial_list = ''
    total = 0
    product = 1
    
    for num in data:
        initial_list = initial_list + str(num) + " "     
    print(initial_list,'\n')
    
    for num in data:
        print(num, ' ', num*num)
 
    for num in data:
        total += num
        product *= num
        
    print('\nThe total of all the values is', total)
    print('The product of all the values is', product, '\n')
          
          
#Output
          
calculate(data1)
calculate(data2)
          
print('\nDone!')
        