def minimum(list1,index=1,mini=0):
    '''
    objective : to find the index of the minimum element
    input parameters :
          list1 : list from which minimum no is to be find
          index : index of next element to be compare
          mini : index of the minimum element in the list
    return value : none
    '''
    if index==len(list1):
        return mini
    else :
        
        if list1[mini] > list1[index]:
           return minimum(list1,index+1,index)
        else :
           return minimum(list1,index+1,mini)

        
