def areaRectangle(length, breadth):
    '''
    objective: to compute the area of rectangle
    input parameters:
        length: length of rectanlgle
        breadth: breadth of the rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    area = length * breadth
    return area
    
def main():
    '''
    objective: to compute the area of rectangle
    user inputs:
        length: length of rectanlgle
        breadth: breadth of the rectangle
    approach: use function areaRectangle
    '''
    
    length = int(input('enter length of rectangle: '))
    breadth = int(input('enter breadth of rectangle: '))
    print('length of rectangle: ', length)
    print('breadth of rectangle: ', breadth)
    print('id(length) : ',id(length))
    print('id(breadth) : ',id(breadth))
    print('id(areaRectangle) : ',id(areaRectangle))
    print('area of rectangle: ',areaRectangle(length, breadth))
    print('End of output')
    
if __name__ == '__main__':
    main()
print('End of program')
