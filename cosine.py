def sine(x):
    '''
    Objective : To find the cosine function of x
    Input paramtrs :
       x : Value of which cosine is need to be found
    Return values :
       result : result cosine value of x
    '''
    #approach : use the series 1-(x^2/2!) + (x^4/4!) ------

    epsilon=0.00001
    term=1
    mulBy=-x*x
    result=1
    nextTerm=1
    while( abs(term)>epsilon):
        divBy=(nextTerm)*(nextTerm+1)
        term*= mulBy/divBy
        result+=term
        nextTerm+=2
    return result

def main():
    '''
    Objective : Computing cosine value
    User input :
        theta : this specifies the value of which cosine to be computed
    '''
    #Approach  : Compute using cosine function
    theta = int(input('Enter the number for which u need to find  a cosine number : '))
    x = (3.14 * theta)/180
    print('The value of cosine ',theta,' is ',sine(x))

if __name__=='__main__':
    main()
