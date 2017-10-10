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
            For Area of Triangle
            base   : base of triangle
            height : height of triangle
    Approach : 
        Compute Area of Triangle using areaTriangle function
    '''
    base   = int(input('Enter the base of Triangle   : '))
    height = int(input('Enter the height of Triangle : '))
    print('\nThe Area of Triangle  is : ',areaTriangle(base,height))

if __name__=='__main__':
    main()
