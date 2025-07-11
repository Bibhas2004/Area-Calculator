while True:
    print("***Area Calculator***")
    print("press 1 to get the area of square\npress 2 to get the are of rectangle\npress 3 to get the area of circle\npress 4 to get the area of triangle\nEnter 'Q' or 'q' to exit the Area Calculator")
    
    choice =int(input("Enter your choice: "))
   
    if choice==1:
        side= int(input("Enter the length of one side: "))
        area=side**2
        print("The area of square: ",area)
    elif choice==2:
        lenght=float(input("Enter the lenght of the rectangle: "))
        width=float(input("Enter the width of the rectangle: "))
        area= lenght*width
        print("The area of rectangle: ",area)
    elif choice==3:
        radius=float(input("Enter the radius of the circle: "))
        area=((22/7)*(radius**2))
        print("The area of circle: ",area)
    elif choice==4:
        base=float(input("Enter the base of the triangle: "))
        height=float(input("Enter the height of the triangle: "))
        area=0.5*base*height
        print("The area of triangle: ",area)
    else:
        print("Invalid Number")
    
    stop=input("Do you want to stop the calculator: ")
    if stop=="yes" or stop=="Yes":
        break
