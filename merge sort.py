def merge(lst1,lst2,list=[]):
    '''
    objective : to perform the merge sort
    input parameters:
                lst1 : first sorted list
                lst2 : second sorted list
                list : list in which final elements are stored
    return value : a sorted list merge by both sorted list
    '''
    if lst1 == [] and lst2 == [] :
        return list

    if lst1 ==[]:
        list.append(lst2[0])
        return merge(lst1,lst2[1:],list)
    elif lst2 == []:
        list.append(lst1[0])
        return merge(lst1[1:],lst2,list)

    else:
        if lst1[0] > lst2 [0]:
            list.append(lst2[0])
            return merge(lst1,lst2[1:],list)
        else:
            list.append(lst1[0])
            return merge(lst1[1:],lst2,list)

            
