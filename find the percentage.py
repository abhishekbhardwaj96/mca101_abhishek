def calcPercent(obtm, maxm):
    '''
    objective: calculate the percentage from the marks being entered
    input parameters:
        obtm: total marks obtained  
        maxm: maximum marks
    approach: divide marks obtained by maximum marks 
              Multiply by 100 and percentage is obtained
    return value: percentage thus calculated is returned
    '''
    percent=(obtm/maxm)*100
    
    return percent
    
def main():
    '''
    objective: calculate the percentage from the marks being entered
    user inputs:
        obtm: total marks obtained  
        maxm: maximum marks
    approach: function call to calPercent is being made
    '''
    
    obtm = int(input('Enter the marks obtained: '))
    maxm = int(input('Enter the maximum marks: '))
    print('Marks obtained: ',obtm)
    print('Maximum marks: ',maxm)
    print('Percentage thus obtained: ',calcPercent(obtm,maxm),'%')
    
if __name__=='__main__':
    main()
