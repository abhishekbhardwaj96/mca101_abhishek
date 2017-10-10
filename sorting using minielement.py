def sorting(list,miniele=0,index=0,index1=0):
    '''
    objective : to sort the given list by finding minielement
    input parameters:
              list: list to be sorted
              miniele:minimum element of unsorted part of list
              index:to maintain the index of list
              index1:index to find the minimum element of list
    return value : sorted list
    '''
    #approach:by using recursion and finding minimum element of list 
    #and swap that with first element of unsorted list
    if index == len(list):
        return list
    elif index1 < len(list):
        if index1==index:
            return sorting(list,list[index],index,index1+1)
            
        elif miniele > list[index1]:
            return sorting(list,list[index1],index,index1+1)
        else:
            return sorting(list,miniele,index,index1+1)
    else:
        temp = list.index(miniele)
        temp1 = list[temp]
        list[temp]=list[index]
        list[index]=temp1
        return sorting(list,0,index+1,0)
#test case
list=[30,40,50,20,10]
sorting(list)
