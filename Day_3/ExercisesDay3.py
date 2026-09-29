
age=20
height=float(5.10)
complex_num=2+3j
print(age, height, complex_num)

base=input("Enter base:")
height=input("Enter height:")
area = float(0.5*float(base)*float(height))
print("The area of the triangle is: ", area)

a=input("Enter side a:")
b=input("Enter side b:")
c=input("Enter side c:")
p=float(float(a)+float(b)+float(c))
print("The perimeter of the triangle is: ", p)


length=float(input("Enter length:"))
width=float(input("Enter width:"))
area=length*width
perimeter=2*(length+width)
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)



r=float(input("Enter the radius of a circle: "))
area_of_circle=3.14*r**2
cricum_of_circle=2*3.14*r
print("The area of the circle is: ", area_of_circle)
print("The circumference of the circle is: ", cricum_of_circle)



#y=m*x+c
m=2
c=-2
slope=m
y_intercept=c
x_intercept=-c/m
print("Slope: ", slope)
print("Y-intercept: ", y_intercept)
print("X-intercept: ", x_intercept)



x1,y1=2,2
x2,y2=6,10
Slope=(y2-y1)/(x2-x1)
print("Slope is:", Slope)
print(Slope>slope)



print(len("python"))
print(len("dragon"))
print(len("python")!=len("dragon"))
print("on" in "python" and "on" in "dragon")



m=("I hope this course is not full of jargon.")
print("jargon" in m)


print("on" not in "dragon" and "on"not in "python")



w1=len("python")
w2=float(w1)
print(str(w2))



x=float(input("Enter a number: "))
if x%2==0:
    print("The number is even.")
else:
    print("The number is odd.")


x=7//3
y=int(2.7)
print(x==y)

print(type('10')==type(10))


print(int(9.8)==10)


h=float(input("Enter hours: "))
r=float(input("Enter rate per hour: "))
pay=h*r
print("Your weekly earning is: ", pay)



y=int(input("Enter the number of years you have lived: ")  )
print("You have lived for ", y*365*24*60*60, " seconds.")


for i in range(1, 6):
    print(i, i**1, i**2, i**3)
