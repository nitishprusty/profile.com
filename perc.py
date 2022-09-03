a = float(input("Enter first side:"))
b = float(input("Enter Second side:"))
c = float(input("Enter Third side:"))

s=(a+b+2)/2
Area = s*(s-a)*(s-b)*(s-b)**0.5
print("The Area of the triangle is",Area)

