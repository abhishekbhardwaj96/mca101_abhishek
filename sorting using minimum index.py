def sorting(list1,index=0):
    '''
    objective : to sort a given list
    input parameters :
            list1 = list to be sort
            index : index of an element we want
    
    return value : none
    '''
    #approach : by calling minimum function recursively to 
    #find minimum element index
    if index== len(list1)-1:
        return list1
    else:
        mini=minimum(list1[index:])
        
        temp = list1[index]
        list1[index] = list1[mini+index]
        list1[mini+index] = temp
        index = index+1
        return sorting(list1,index)
        
def minimum(list1,index=1,mini=0):
    '''
    objective : to find the index of the minimum element
    input parameters :
    list1 : list from which minimum no is to be find
    index : index of next element to be compare 
    mini : index of the minimum element in the list
    return value : none
    '''
    #approach : using recursion
    if index==len(list1):
        return mini
    else :
        if list1[mini] > list1[index]:
            return minimum(list1,index+1,index)
        else :
            return minimum(list1,index+1,mini)
list=[10,50,30,5,20]
sorting(list)
