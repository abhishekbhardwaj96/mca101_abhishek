def Tower_Of_Hanoi(discs,source,spare,target) :
    '''
    Objective : To Implement Tower Of Hanoi having 3 poles
    Input Paramtrs : 
        discs  : No of discs 
        source : Source Pole from which disk is to be move
        spare  : Intermediate Pole through which disk is to be move
        target : Target Pole fianlly at which pole disk is to be move
    '''
    # Approach : Implementing TOH using recursion 
    if discs == 1 :
        print('Move Disc From ',source,' to ',target)
    else :    
        Tower_Of_Hanoi(discs-1,source,target,spare)
        Tower_Of_Hanoi(1,source,spare,target)
        Tower_Of_Hanoi(discs-1,spare,source,target)

print(Tower_Of_Hanoi(4,1,3,2))
