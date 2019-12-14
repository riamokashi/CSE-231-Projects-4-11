###########################################
#
# COMPUTER PROJECT #4

# functions 

#   Make function within a function  
  
#    make multiple functions 

#       calculate sum_natural

#       calculate approximate_euler

#       calculate approximate_sinh

#       calculate approximate_cosh

#       find difference between real value and approximate value 

##################################################

import math
#define epsilon as a constant value that will be used later 
EPSILON = 1.0e-7

def display_options():
    # display the menu of option 
    ''' This function displays the menu of options'''

    MENU = '''\nPlease choose one of the options below:
             A. Display the value of the sum of the first N natural numbers. 
             B. Display the approximate value of e.
             C. Display the approximate value of the hyperbolic sine of X.
             D. Display the approximate value of the hyperbolic cosine of X.
             M. Display the menu of options.
             X. Exit from the program.'''
       
    print(MENU)
    
def sum_natural(N):
    '''This function calculates the sum natural'''
    # define sum so that it can be added to later 
    sum_n = 0
    for num in range(0, sum_n+1, 1):
        # iterate through n values until it reaches N
        # calculate sum as you go through each value 
        sum_n = sum_n + num
    return (sum_n)
     


def approximate_euler():
    '''This function calculates the approximate euler function'''
    # define values that will be used later 
    term = 1
    e = 0 
    k = 0
    # create while loop to iterate though the calculations until it reaches EPSILON, then stop
    while abs(term) >= EPSILON:
        # define a math equation for the term 
        term = 1/math.factorial(k)
        # take the abs of the term because it cannot be negative according to the equation
        e += abs(term)
        # keep adding one
        k += 1
    # define the values that will be printed 
    approximation = round(e,10)
    math_module = round(math.e, 10)
    difference = math_module - approximation
    return (approximation)
    return (math_module)
    return (difference)
   
    
def approximate_sinh(x):
    '''This function calculates the approximate sin value'''
    # ask for an input 'X' to calculate the sin
    input_sin = input("Enter an integer X: ")
    input_sin = int(input_sin)
    # math euqation for the approximation for sin
    approximation = round(((x)**((2)(input_sin))/(math.factoial((2)(input_sin)))), 10)
    # real value of sin
    math_module = round(math.sinh(float(input_sin)), 10)
    # calculate the difference between real and approximation
    difference = math_module - approximation 
    return (approximation)
    return (math_module)
    return (difference)
           
def approximate_cosh(x):
    '''this function calculates the approximate cos value'''
    # ask for an input 'X' to calculate the cos
    input_cos = input("Enter an integer X: ")
    # convert to an int to do the math
    input_cos = int(input_cos)
    # math euqation for the approximation for cos
    approximation = round(((x)**((2)(input_cos) + 1))/(math.factoial((2)(input_cos) + 1)), 10)
    # real value of cos
    math_module = (round(math.sinh(float(input_cos)), 10))
    # calculate the difference between real and approximation
    difference = math_module - approximation 
    return (approximation)
    return (math_module)
    return (difference)

def main():
    print("A.Display the value of the sum of the first natural numbers")
    print("B.Display the approximate value of e")
    print("C.Dsplay the approximate value of the hyperbolic sine of x")
    print("D.Display the approximate value of the hyprebolic cosine of x")
    print("M.Display the menu of items.")
    print("X.Exit the program.")
    INPUT = input('Option: ')
    while INPUT:
        if INPUT == 'A' or INPUT == 'a':
            N = input('enter an integer N')
            if N.isdigit():
                N = int(N)
                print(sum_natural(N))
                break
            else: 
                print('None')
                break
        elif INPUT == 'B' or INPUT == 'b':
            print(approximate_euler())
            break
        elif INPUT == 'C' or INPUT == 'c':
            x = input("Enter X: ")
            print(approximate_sinh(x))
            break
        elif INPUT == 'D':
            x = input("Enter X: ")
            print(approximate_cosh(x))
            break
        elif INPUT == 'M':
            display_options()
            
        elif INPUT == 'X':   
            print("Hope to see u again! !")
            break
        else:
            print("Error  Unrecognized option " , INPUT)
            break
    

if __name__ == "__main__": 
    main()