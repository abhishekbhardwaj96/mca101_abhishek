def increment(number):
    '''
     objective : to increase the number enter by user by 1 
     input parameter :
            number : number to be incremented
     return value : number as incremented by 1
     '''
    number = number+1
    return number

def add(num1,num2):
    '''
    objective : to calculate the sum of two numbers
    input parameters :
          num1: first number enter by user
          num2: second number enter by user
          return value : sum of two number
    '''
    # approach : sum of two number by increment function
    assert num1 >= 0 and num2 >= 0
    if num2 == 0:
       return num1
    else:
       return add(increment(num1),num2-1)
