def midTriangle(s):
    '''
    objective: draw an isosceles triangle
    Input parameter:
        s: symbol used to draw the triangle
    approach: using function and sending the symbol to the function as a parameter
    '''
    print('    ',s,'    ') 
    print('   ',s,s,'   ')
    print('  ',s,s,s,'  ')
    print(' ',s,s,s,s,' ')
    
def main():
    '''
    objective: to display the isosceles triangle
    User Input:
        symbol: the symbol used to draw the triangle
    approach: use of midTriangle function
    '''
    print('Enter the symbol: ')
    symbol = input()
    print('Symbol entered is: ',symbol)
    midTriangle(symbol)
    
if __name__=='__main__':
    main()
