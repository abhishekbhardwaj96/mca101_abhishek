def sine(x):
    '''
    Objective : To find the sine function of x
    Input paramtrs :
       x : Value of which sine is need to be found
    Return values :
       result : result sine value of x
    '''
    #approach : use the series x-(x^3/3!) + (x^5/5!) ------

    epsilon=0.00001
    term=x
    mulBy=-x*x
    result=x
    nextTerm=2
    while( abs(term)>epsilon):
        divBy=(nextTerm)*(nextTerm+1)
        term*= mulBy/divBy
        result+=term
        nextTerm+=2
    return result

def main():
    '''
    Objective : Computing sine value
    User input :
        theta : this specifies the value of which sine to be computed
    '''
    #Approach  : Compute using sine function
    theta = int(input('Enter the number for which u need to find  a sine number : '))
    x = (3.14 * theta)/180
    print('The value of sine ',theta,' is ',sine(x))

if __name__=='__main__':
    main()
