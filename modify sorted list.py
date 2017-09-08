def insInSortedList(list1,num,count=0):
    '''
    objective : to modify a sorted list
    input parameters:
               list1 : sorted list to be modify
               num : number enter in a list
    approach : by calling function recursively
    return value : none
    '''
    x=len(list1)
    if (num < list1[count]):
        list1.insert(count,num)
        return list1
    elif count ==x:
        list1.append(num)
        return list1
    else:
        return insInSortedList(list1,num,count+1)

