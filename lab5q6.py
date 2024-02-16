'''
Do not remove any text from these comments
6.	Modify the Python program for Question 5 to allow my_list 
data to be deleted if a list index is an even number when 
decrementing the list index in a loop.

my_list = []
Enter an integer data: 1
Enter a string: HELLO
Enter a string: AB
Enter a list data: [1.0, -1, 'A']
Enter a float data: 0.1
my_list = [1.0, 'HELLO', 'AB', [1.0, -1, 'A'], 0.1]
my_list = [1.0, 'HELLO', 'AB', [1.0, -1, 'A']]
my_list = [1.0, 'HELLO', 'AB', [1.0, -1, 'A']]
my_list = [1.0, 'HELLO', [1.0, -1, 'A']]
my_list = [1.0, 'HELLO', [1.0, -1, 'A']]
my_list = ['HELLO', [1.0, -1, 'A']]


Function to use: float(), input(), print(), ast.literal_eval(), 
keyword: del
Operators: +, -, >=
Structure: while, if
'''
import ast
def main():
    my_list = []
    count = 1
 
    num = float(input("Enter an integer data: "))
    num1 = input("Enter a String data: ")
    num2 = input("Enter a String data: ")
    num3 = ast.literal_eval(input("Enter a list data: "))
    num4 = float(input("Enter a float data: "))

    my_list = [num, num1, num2, num3, num4]

    print("my_list =" , my_list)

    lastindex = 4
    while lastindex >= 0:
        del my_list[lastindex]
        print("my_list =" , my_list)
        lastindex = lastindex - 1
    return 0



