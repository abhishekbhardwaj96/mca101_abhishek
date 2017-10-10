def areaRectangle(length,breadth):
    '''
    Objective : to find the area of Rectangle
    Input Paramters :
        length  : length of rectangle
        breadth : breadth of rectangle
    Approach  : multiply length and breadth
    Return Values : return area of rectangle
    '''
    area = length * breadth
    return area
    
def areaTriangle(base,height):
    '''
    Objective : to find the area of Triangle
    Input Paramters :
        base   : base of triangle
        height : height of triangle
    Approach  : multiply base and height and then divide by 2
    Return Values : return area of triangle
    '''
    area = (1/2) * base * height
    return area
    
def main():
    '''
    Objective : To find area of Rectangle or Triangle
    User inputs :
        For Area Of Rectangle
            length  : length of rectangle
            breadth : breadth of rectangle
        For Area of Triangle
            base   : base of triangle
            height : height of triangle
    Approach : 
        Compute Area of Rectangle using areaRectangle function
        Compute Area of Triangle using areaTriangle function
    '''
    areaType = input('Which area you want to find (Rectangle/Triangle) : ')
    if areaType == 'Rectangle':
        print('\t\t============================= ')
        print('\t\t Computing Area Of Rectangle ')
    
        length  = int(input('Enter the length of Rectangle  : '))
        breadth = int(input('Enter the breadth of Rectangle : '))
        print('\nThe Area of Rectangle is : ',areaRectangle(length,breadth))
    
    elif areaType == 'Triangle':
        print('\t\t============================= ')
        print('\t\t Computing Area of Triangle ')
        base   = int(input('Enter the base of Triangle   : '))
        height = int(input('Enter the height of Triangle : '))
        print('\nThe Area of Triangle  is : ',areaTriangle(base,height))

if __name__=='__main__':
    main()
